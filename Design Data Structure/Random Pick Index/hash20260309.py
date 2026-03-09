class Solution:
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for i in range(len(nums)):
            self.map[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        if len(self.map[target])!=0:
            index = random.choice(self.map[target])
            return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)