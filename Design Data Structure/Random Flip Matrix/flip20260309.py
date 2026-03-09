import random
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        # 抽象的一尾数组的长度
        self.len = m*n
        self.deletedToExist = {} # 已经删除元素到尾部未删除元素的映射
        self.random = random.Random()

    def flip(self) -> List[int]:
        rand = self.random.randint(0, self.len-1)
        res = rand
        if rand in self.deletedToExist:
            res = self.deletedToExist[rand]
        # 将rand置换到数组的尾部
        last = self.len-1
        # 尾部的元素也有可能已经被删掉了
        if last in self.deletedToExist:
            last = self.deletedToExist[last]
        self.deletedToExist[rand] = last
        self.len-=1 # 删除尾部的元素
        # 一维左边转换为二维
        return [res//self.n, res%self.n]
    
    def reset(self):
        self.len = self.m*self.n
        self.deletedToExist.clear()
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()