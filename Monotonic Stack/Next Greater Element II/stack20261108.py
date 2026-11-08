class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        new_nums = nums*2
        ans = [-1]*len(nums)
        st = []
        for i in range(len(new_nums)):
            while st and new_nums[st[-1]]<new_nums[i]:
                ans[st[-1]%len(nums)] = new_nums[i]
                st.pop()
            st.append(i%len(nums))
        return ans
