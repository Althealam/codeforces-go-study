# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n^2)
# 对于长度为n的数组，单次递归需要O(n)的时间：找最大值需要O(n)，找index需要O(n)，切片需要O(k)
# 如果每次最大值刚好都在数组的最左边或者最右边，那么递归规模会变成T(n)=T(n-1)+O(n)
# 即T(n) = O(n+(n-1)+...+1)=O(n^2)

# 空间复杂度：O(n^2)
# Python切片会创建新的列表，因此nums[:root_index]会产生新的数组，并且递归深度最坏为n，每次递归的空间复杂度为O(n)，因此最终的空间复杂度为O(n^2)
# 最坏情况下：[1, 2, 3, 4, 5]，此时需要递归5次，每次递归都要创建一个O(n)的数组
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        if len(nums)==0:
            return None
        root_val = max(nums)
        root = TreeNode(root_val)
        root_index = nums.index(root_val)
        root.left = self.constructMaximumBinaryTree(nums[:root_index])
        root.right = self.constructMaximumBinaryTree(nums[root_index+1:])
        return root