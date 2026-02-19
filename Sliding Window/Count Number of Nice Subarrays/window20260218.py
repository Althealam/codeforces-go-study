# the number of nice subarrays = the number of subarrays which have at most k odd numbers - the number of subarrays which have at most k-1 odd numbers
# [1, 1, 2, 1, 1] k =3
# left = 0, right = 1: [1], [1, 1]
# at most k odd numbers: [1], [1], [1, 1], [1, 1, 2], [1, 2, 1], [1, 2, 1, 1], [2, 1, 1], [1, 1], [1], [1], [1, 1, 2, 1]
# at most k-1 odd numbers: [1], [1], [1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 1], [1], [1]
# left=right=0: [1]
# left=0, right=1: [1, 1], [1]
# left=0, right=2: [1, 1, 2], [1, 2], [2]
# left=0, right=3: [1, 1, 2, 1], [1, 2, 1], [2, 1], [1]
# left=0, right=4: [1, 1, 2, 1, 1]
# left=1, right=4: [1, 2, 1, 1], [2, 1, 1], [1, 1], [1]

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # print(self.get_most(nums, k))
        return self.get_most(nums, k)-self.get_most(nums, k-1)

    def get_most(self, nums, k):
        num_of_odd = 0
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                num_of_odd+=1

            while num_of_odd>k:
                if nums[left]%2!=0:
                    num_of_odd-=1
                left+=1
            if num_of_odd<=k:
                count+=right-left+1
        return count

nums = [1, 1, 2, 1, 1]
k = 3
sol = Solution()
res = sol.numberOfSubarrays(nums, k)
print(res)