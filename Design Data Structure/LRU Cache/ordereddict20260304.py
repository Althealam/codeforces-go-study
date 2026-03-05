# cache = Orderdict()
# put(1, 1): cache[1] = 1
# put(2, 2): cache[2] = 2
# get(1): return cache[1]
# put(3, 3): cache[3] = 3
# get(2): return cache[2]

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # change the direction
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value

        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)