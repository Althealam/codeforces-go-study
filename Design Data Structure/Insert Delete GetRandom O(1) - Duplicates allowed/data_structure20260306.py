class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.idx[val])==1 # 如果之前没有这个元素，返回True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        remove_index = self.idx[val].pop()
        last_val = self.nums[-1]
        last_index = len(self.nums)-1
        if remove_index!=last_index:
            self.nums[remove_index] = last_val
            
            # 更新last_val的index
            self.idx[last_val].remove(last_index)
            self.idx[last_val].add(remove_index)
        
        # 删除最后一个元素
        self.nums.pop()

        # 如果val已经没有index了，删除key
        if len(self.idx[val])==0:
            del self.idx[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()