# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
from typing import cast
from xml.etree.ElementTree import ElementTree, SubElement, QName
import isodate

# Refer to the async version of this module under ..\aio\management\_utils.py for detailed explanation.

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse  # type: ignore  # for python 2.7

from azure.servicebus.management import _constants as constants
from ._handle_response_error import _handle_response_error


def extract_rule_data_template(feed_class, convert, feed_element):
    deserialized = feed_class.deserialize(feed_element)
    next_link = None
    if deserialized.link and len(deserialized.link) == 2:
        next_link = deserialized.link[1].href
    if deserialized.entry:
        list_of_entities = [
            convert(*x) if convert else x for x in zip(
                feed_element.findall(constants.ATOM_ENTRY_TAG), deserialized.entry)
        ]
    else:
        list_of_entities = []
    return next_link, iter(list_of_entities)


def extract_data_template(feed_class, convert, feed_element):
    deserialized = feed_class.deserialize(feed_element)
    list_of_entities = [convert(x) if convert else x for x in deserialized.entry]
    next_link = None
    if deserialized.link and len(deserialized.link) == 2:
        next_link = deserialized.link[1].href
    return next_link, iter(list_of_entities)


def get_next_template(list_func, *args, **kwargs):
    start_index = kwargs.pop("start_index", 0)
    max_page_size = kwargs.pop("max_page_size", 100)
    api_version = constants.API_VERSION
    if args[0]:
        queries = urlparse.parse_qs(urlparse.urlparse(args[0]).query)
        start_index = int(queries[constants.LIST_OP_SKIP][0])
        max_page_size = int(queries[constants.LIST_OP_TOP][0])
        api_version = queries[constants.API_VERSION_PARAM_NAME][0]
    with _handle_response_error():
        feed_element = cast(
            ElementTree,
            list_func(
                skip=start_index, top=max_page_size,
                api_version=api_version,
                **kwargs
            )
        )
    return feed_element


def deserialize_value(value, value_type):
    if value_type in ("int", "long"):
        value = int(value)
    elif value_type == "boolean":
        value = value.lower() == "true"
    elif value_type == "double":
        value = float(value)
    elif value_type == "dateTime":
        value = isodate.parse_datetime(value)
    elif value_type == "duration":
        value = isodate.parse_duration(value)
    return value


def serialize_value_type(value):
    value_type = type(value)
    if value_type == str:
        return "string", value
    if value_type == int:
        return "int" if value <= constants.INT_MAX_VALUE_CSHARP else "long", str(value)
    if value_type == float:
        return "double", str(value)
    if value_type == bool:
        return "boolean", str(value).lower()
    if value_type == datetime:
        return "dateTime", isodate.datetime_isoformat(value)
    if value_type == timedelta:
        return "duration", isodate.duration_isoformat(value)
    raise ValueError("value {} of type {} is not supported for the key value".format(value, value_type))


def deserialize_key_values(root, key_values):
    key_values_ele = root.findall(constants.RULE_KEY_VALUE_TAG)
    for key_value_ele in key_values_ele:
        key_ele = key_value_ele.find(constants.RULE_KEY_TAG)
        value_ele = key_value_ele.find(constants.RULE_VALUE_TAG)
        key = key_ele.text
        value = value_ele.text
        value_type = value_ele.attrib[constants.RULE_VALUE_TYPE_TAG]
        value_type = value_type.split(":")[1]
        value = deserialize_value(value, value_type)
        key_values[key] = value


def deserialize_rule_key_values(entry_ele, rule_description):
    content = entry_ele.find(constants.ATOM_CONTENT_TAG)
    if content:
        correlation_filter_properties_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_FILTER_TAG) \
            .find(constants.RULE_FILTER_COR_PROPERTIES_TAG)
        if correlation_filter_properties_ele:
            deserialize_key_values(correlation_filter_properties_ele, rule_description.filter.properties)
        sql_filter_parameters_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_FILTER_TAG) \
            .find(constants.RULE_PARAMETERS_TAG)
        if sql_filter_parameters_ele:
            deserialize_key_values(sql_filter_parameters_ele, rule_description.filter.parameters)
        sql_action_parameters_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_ACTION_TAG) \
            .find(constants.RULE_PARAMETERS_TAG)
        if sql_action_parameters_ele:
            deserialize_key_values(sql_action_parameters_ele, rule_description.action.parameters)


def serialize_key_values(xml_parent, key_values):
    """serialize a dict to xml Element and put it under xml_parent

    The serialized XML is like:

    <KeyValueOfstringanyType>
        <Key>key_string</Key>
        <Value xmlns:d6p1="http://www.w3.org/2001/XMLSchema" xsi:type="d6p1:string">str1</Value>
    </KeyValueOfstringanyType>
    <KeyValueOfstringanyType>
        <Key>key_int</Key>
        <Value xmlns:d6p1="http://www.w3.org/2001/XMLSchema" xsi:type="d6p1:int">2</Value>
    </KeyValueOfstringanyType>
    ...

    :param xml_parent: The parent xml Element for the serialized xml.
    :param key_values: The dict that contains the key values.
    :return: `xml_parent` is mutated. The returned value is `None`.
    """
    xml_parent.clear()
    if key_values:
        for key, value in key_values.items():
            value_type, value_in_str = serialize_value_type(value)
            key_value_ele = SubElement(xml_parent, QName(constants.SB_XML_NAMESPACE, constants.RULE_KEY_VALUE))
            key_ele = SubElement(key_value_ele, QName(constants.SB_XML_NAMESPACE, constants.RULE_KEY))
            key_ele.text = key
            type_qname = QName(constants.XML_SCHEMA_INSTANCE_NAMESPACE, "type")
            value_ele = SubElement(
                key_value_ele, QName(constants.SB_XML_NAMESPACE, constants.RULE_VALUE),
                {type_qname: constants.RULE_VALUE_TYPE_XML_PREFIX + ":" + value_type}
            )
            value_ele.text = value_in_str
            value_ele.attrib["xmlns:"+constants.RULE_VALUE_TYPE_XML_PREFIX] = constants.XML_SCHEMA_NAMESPACE


def serialize_rule_key_values(entry_ele, rule_descripiton):
    """Serialize a rule's filter and action that have key values into xml.

    CorrelationRuleFilter.properties, SqlRuleFilter.parameters and SqlRuleAction.parameters may contain
    data (dict is not empty). Serialize them to XML.

    """
    content = entry_ele.find(constants.ATOM_CONTENT_TAG)
    if content:
        correlation_filter_parameters_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_FILTER_TAG) \
            .find(constants.RULE_FILTER_COR_PROPERTIES_TAG)
        if correlation_filter_parameters_ele:
            serialize_key_values(correlation_filter_parameters_ele, rule_descripiton.filter.properties)
        sql_filter_parameters_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_FILTER_TAG) \
            .find(constants.RULE_PARAMETERS_TAG)
        if sql_filter_parameters_ele:
            serialize_key_values(sql_filter_parameters_ele, rule_descripiton.filter.parameters)
        sql_action_parameters_ele = content\
            .find(constants.RULE_DESCRIPTION_TAG) \
            .find(constants.RULE_ACTION_TAG) \
            .find(constants.RULE_PARAMETERS_TAG)
        if sql_action_parameters_ele:
            serialize_key_values(sql_action_parameters_ele, rule_descripiton.action.parameters)
