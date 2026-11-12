# 核心思路：维护一个前缀积数组，让getProduct(k)能够在O(1)时间内计算最后k个数字的乘积
# pre[i] = nums[0]*nums[1]*...*nums[i-1]
# 最直接的做法：保存所有数字，每次调用getProduct(k)时遍历最后k个数字
# nums= [3, 4, 2, 5]
# pre = [1, 3, 12, 24, 120]
# 计算最后两个元素的乘积
# 2*5 = 3*4*2*5 / 3*4 = pre[-1] / pre[-k-1]

class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]        

    def add(self, num: int) -> None:
        if num==0:
            self.pre = [1] # 当num=0时，需要重新开始计算前缀和
        else:
            self.pre.append(self.pre[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if k>=len(self.pre):
            return 0
        return self.pre[-1]//self.pre[-(k+1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)