# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6246, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class IndexActionType(str, Enum):
    """The operation to perform on a document in an indexing batch.
    """

    upload = "upload"
    merge = "merge"
    merge_or_upload = "mergeOrUpload"
    delete = "delete"

class QueryType(str, Enum):

    simple = "simple"
    full = "full"

class SearchMode(str, Enum):

    any = "any"
    all = "all"

class AutocompleteMode(str, Enum):

    one_term = "oneTerm"
    two_terms = "twoTerms"
    one_term_with_context = "oneTermWithContext"
