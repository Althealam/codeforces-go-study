# nums = []
# val_index = defaultdict(set) e.g: {1: [0, 1], 2: [2, 3]}

# 1. insert
# (1) if val not in val_index:
# - update index in the val_index
# - append the val into the nums
# - return True
# (2) if val in val_index:
# - update index in the val_index
# - append the val into the nums
# - return False

# 2. remove
# (1) if val in val_index:
# - get all the index for val
# - find the delete index for val
# - change the place for delete element and last element
# - update index for the last element
# - pop the last element from nums
# - return True
# (2) if val not in val_index:
# - return False

# 3. getRandom
# choice.random(nums)
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.val_index = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val not in self.val_index:
            self.val_index[val].add(len(self.nums))
            self.nums.append(val)
            return True
        else:
            self.val_index[val].add(len(self.nums))
            self.nums.append(val)
            return False

    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        else:
            remove_index = self.val_index[val].pop()
            exchange_val = self.nums[-1]
            exchange_index = len(self.nums)-1
            if remove_index!=exchange_index:
                self.nums[remove_index] = exchange_val
                self.val_index[exchange_val].remove(exchange_index) # set是无序的，并且没有重复元素的，因此直接删除index的时间复杂度是O(1)
                self.val_index[exchange_val].add(remove_index)
            
            self.nums.pop()
            if len(self.val_index[val])==0:
                del self.val_index[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()