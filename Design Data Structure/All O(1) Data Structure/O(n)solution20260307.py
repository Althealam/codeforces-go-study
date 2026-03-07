
class AllOne:
    def __init__(self):
        self.key_freq = {}
        self.freq_key = defaultdict(set)
        self.min_freq = float('inf')
        self.max_freq = float('-inf')

    def inc(self, key: str) -> None:
        if key in self.key_freq:
            old_frequency = self.key_freq[key]
            self.freq_key[old_frequency].remove(key)
            if len(self.freq_key[old_frequency])==0:
                del self.freq_key[old_frequency]
            self.key_freq[key]+=1
            new_frequency = self.key_freq[key]
            self.freq_key[new_frequency].add(key)
        else:
            self.key_freq[key] = 1
            self.freq_key[1].add(key) 
        self.max_freq = max(self.key_freq.values())
        self.min_freq = min(self.key_freq.values())
        
    

    def dec(self, key: str) -> None:
        old_frequency = self.key_freq[key]
        self.freq_key[old_frequency].remove(key)
        if len(self.freq_key[old_frequency])==0:
            del self.freq_key[old_frequency]
        self.key_freq[key]-=1
        if self.key_freq[key]==0:
            del self.key_freq[key]
        else:
            new_frequency = self.key_freq[key]
            self.freq_key[new_frequency].add(key)
        if len(self.key_freq)!=0:
            self.max_freq = max(self.key_freq.values())
            self.min_freq = min(self.key_freq.values())
        

    def getMaxKey(self) -> str:
        # cannot do the list(self.freq_key)
        return next(iter(self.freq_key[self.max_freq])) if self.max_freq in self.freq_key and self.freq_key[self.max_freq] else ""        

    def getMinKey(self) -> str:
        return next(iter(self.freq_key[self.min_freq])) if self.min_freq in self.freq_key and self.freq_key[self.min_freq] else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()