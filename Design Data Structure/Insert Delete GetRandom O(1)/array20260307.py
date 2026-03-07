# value_index = {} e.g: {1: 0, 2: 1, 2: 2}
# nums = [] e.g: nums=[1, 2, 2]
 
# 1. insert
# 2. remove
# 3. getRandom

import random
class RandomizedSet:
    def __init__(self):
        self.value_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.value_index:
            self.value_index[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.value_index:
            exchange_val = self.nums[-1]
            exchange_index = len(self.nums)-1
            delete_index = self.value_index[val]
            self.value_index[exchange_val] = delete_index
            del self.value_index[val]
            self.nums[delete_index] = exchange_val
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()