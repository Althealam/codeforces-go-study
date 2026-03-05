
class LFUCache:

    def __init__(self, capacity: int):
        self.key_value = {}
        self.key_freq = {}
        self.freq_map = defaultdict(OrderedDict)
        self.capacity = capacity
        self.min_freq = 0
        
    def get(self, key: int) -> int:
        # === key isn't in the self.key_value
        if key not in self.key_value:
            return -1
        # === key is in the self.key_value
        # current frequence
        freq = self.key_freq[key]
        # delete from the old freq bucket
        del self.freq_map[freq][key]
        # if this freq bucket is None and this is the smallest freq
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq==freq:
                self.min_freq+=1
        # update frequence
        new_freq = freq+1
        self.key_freq[key] = new_freq
        # add into the new freq bucket
        self.freq_map[new_freq][key] = None
        return self.key_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity ==0:
            return 
        
        if key in self.key_value:
            self.key_value[key] = value
            self.get(key) # update frequence by using get
            return 
        
        # key isn't in the cache, then we have to check the length of the cache first 
        if len(self.key_value)>=self.capacity:
            # the least freq bucket
            # NOTE: Cannot use min(self.freq_map), cause it will take O(n) complexity
            freq_bucket = self.freq_map[self.min_freq]

            # delete LRU key
            evict_key, _ = freq_bucket.popitem(last=False)

            del self.key_value[evict_key]
            del self.key_freq[evict_key]
            
            if not freq_bucket:
                del self.freq_map[self.min_freq]

        # insert new key
        self.key_value[key] = value
        self.key_freq[key] = 1
        self.freq_map[1][key] = None
        self.min_freq = 1

        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)