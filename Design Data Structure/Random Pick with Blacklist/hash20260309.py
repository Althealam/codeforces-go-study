# input: n, blacklist
# self.map = {}
# self.array = []

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.sz = n-len(blacklist)
        self.mapping = {}

        blackSet = set(blacklist)
        last = n-1
        for b in blacklist: 
            # b已经在[sz, n]的区间内
            if b>=self.sz:
                continue
            # 跳过所有黑名单中的数组
            while last in blackSet:
                last-=1
            # 将黑名单中的索引映射到合法的数字
            self.mapping[b] = last
            last-=1
        
        

    def pick(self) -> int:
        # 随机选择一个索引
        index = random.randint(0, self.sz-1)
        # 这个索引命中了黑名单，需要被映射到其他位置
        if index in self.mapping:
            return self.mapping[index]
        # 如果没有命中黑名单，则直接返回
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()