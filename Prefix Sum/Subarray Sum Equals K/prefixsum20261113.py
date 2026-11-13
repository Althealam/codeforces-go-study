# pre[j]-pre[i] = k
# pre[i] = pre[j]-k 
# target = pre[j]-k -> 对当前j而言，要找到和为k的子数组，因此需要寻找之前是否存在前缀和为pre[i]=pre[j]-k的值
# hash的key为前缀和，value为出现次数：同一个目标前缀和每出现一次，就代表一个满足条件的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1]+nums[i]
        hash = {} # 哈希表中value存储出现次数，而不是下标，key为pre[i]

        # 当value为频率，而不是下标时，初始化为hash[0] = 1
        hash[0] = 1
        ans = 0
        for i in range(len(pre)):
            target = pre[i]-k
            if target in hash:
                ans+=hash[target]
            if pre[i] not in hash:
                hash[pre[i]] = 1
            else:
                hash[pre[i]] +=1
        return ans
        