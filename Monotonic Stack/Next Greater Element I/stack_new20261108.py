# 1. 单调栈中存储nums2中还没有找到下一个更大元素i的元素下标
# 2. 定义一个map存储nums1的下标和值的map
# 3. 遍历nums2，找到每个元素的下一个更大元素
# 4. 利用map还原nums1的情况
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = [-1]*len(nums1)
        st = []
        hash_map = {}
        for i in range(len(nums1)):
            hash_map[nums1[i]] = i
        for i in range(len(nums2)):
            while st and st[-1]<nums2[i]:
                # handle the ans for st[-1]
                if st[-1] in nums1:
                    ans[hash_map[st[-1]]] = nums2[i]
                st.pop()
            st.append(nums2[i])
        return ans
        