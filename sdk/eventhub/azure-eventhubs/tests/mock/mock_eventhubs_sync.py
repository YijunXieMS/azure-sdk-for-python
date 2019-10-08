import time
import datetime
from queue import SimpleQueue
import uamqp
from azure.eventhub import EventData


class MessageStoreSync(object):
    def __init__(self, p_qty=None):
        self._p_qty = p_qty
        self._pids = range(p_qty)
        self._stores = [SimpleQueue() for _ in range(p_qty)]
        self._round_robin_counter = 0
        self.offset = 0
        self.sn = 0

    def save_message(self, msg, pid=None):
        annotations = {}
        annotations[EventData.PROP_OFFSET] = self.offset
        annotations[EventData.PROP_SEQ_NUMBER] = self.sn
        annotations[EventData.PROP_TIMESTAMP] = datetime.datetime.now().timestamp() * 1000
        msg.annotations = annotations

        if pid is None:
            self._stores[self._round_robin_counter].put(msg)
            if self._round_robin_counter >= self._p_qty:
                self._round_robin_counter -= self._p_qty
        else:
            self._stores[int(pid)].put(msg)

        self.sn += 1
        self.offset += 100

    def retrieve_messages(self, pid, size, timeout):
        start = time.time()
        n = size
        result = []
        p = int(pid)
        while n > 0 and time.time() - start <= timeout / 1000:
            try:
                result.append(self._stores[p].get_nowait())
            except:
                pass
            n -= 1
            time.sleep(0.001)
        return result
