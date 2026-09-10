# 需要找到nums1[i]+nums2[j]=-(nums3[k]+nums4[l])
# 需要记录某个组合出现了多少次

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2) 因为hash_map最坏情况下需要存储nums1+nums2所有不同的两数之和
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 in hash_map:
                    hash_map[num1+num2]+=1
                else:
                    hash_map[num1+num2]=1
        
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in hash_map:
                    ans+=hash_map[-(num3+num4)]
        return ans