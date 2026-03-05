from collections import OrderedDict
class MRUQueue:
    def __init__(self, n):
        self.queue = OrderedDict()
        for i in range(1, n+1):
            self.queue[i] = None

    def fetch(self, k):
        for i in range(1, len(self.queue)+1):
            if i==k:
                target = k
                break
        del self.queue[target]
        self.queue[target] = None # 放到队尾
        return target

mru = MRUQueue(8)
mru.fetch(3)
