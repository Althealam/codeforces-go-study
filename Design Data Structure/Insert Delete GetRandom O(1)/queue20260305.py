# NOTE: if val in queue ==> need O(n) time complexity
# NOTE: queue.pop(index) ==> need O(n) time complexity

# self.randomizedset = queue()
# self.val_index = {}

# 1. insert: 
# (1) if val not in self.val_index
# - self.val_index[val] = len(self.val_index)
# - self.randomizedset.append(val)
# - return True
# (2) if val in self.val_index: return False

# 2. remove
# (1) if val in self.val_index
# - exchange place: 
# current_index = self.val_index[val]
# exchange_index = len(self.randomizedset)-1
# current_val, exchange_val = val, self.randomizedset[-1]
# self.randomizedset[current_index], self.randomizedset[exchange_index] = self.randomizedset[exchange_index], self.randonmizedset[current_index]
# self.randomizedset.pop()
# self.val_index[exchange_val] = current_index
# del self.val_index[current_val]

# (2) if val not in self.val_index: return False

# 3. getRandom
# random_index = random.choice(len(self.randomizedset))
# return self.randomizedset[random_index]

from collections import deque
import random
class RandomizedSet:
    def __init__(self):
        self.randonmizedset = deque()
        self.val_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        self.val_index[val] = len(self.val_index)
        self.randonmizedset.append(val)
        return True
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        # get the index and val
        current_index = self.val_index[val]
        exchange_index = len(self.randonmizedset)-1
        current_val, exchange_val = val, self.randonmizedset[-1]

        # exchange the place in randonmizedset
        self.randonmizedset[current_index], self.randonmizedset[exchange_index] = self.randonmizedset[exchange_index], self.randonmizedset[current_index]

        # pop the value from the end of the set
        self.randonmizedset.pop()

        # update the index 
        self.val_index[exchange_val] = current_index
        del self.val_index[current_val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.randonmizedset)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()