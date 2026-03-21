# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root(TreeNode), voyage(list)
# output: values of all flipped nodes (list[int])

# 1. 是否需要遍历所有节点：是的
# 2. 是否依赖子节点的返回值：否，因此是traversal类型的题目
# 3. 什么时候操作，以及需要做什么
# if root.val==voyage[index]
# - 判断一下root.left和voyage的下一个元素是否匹配
# * 如果匹配的话，则继续先遍历root.left，再遍历右子树
# * 如果不匹配的话，说明root需要进行反转，将其加入到flipped数组中，然后先遍历root.right，再遍历root.left
# if root.val!=voyage[index]: 当前不匹配，直接return [-1]

class Solution:
    def __init__(self):
        self.index = 0 # 当前遍历的索引
        self.flipped = [] # 存储需要反转的节点的值

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if self.traversal(root, voyage):
            return self.flipped
        else:
            return [-1]
    
    def traversal(self, root, voyage):
        if root is None: # 这个分支是空的，但是没有违反任何规则
            return True # 注意：空节点是合法的，不可以直接写return（相当于return None)，必须是return True
        if root.val!=voyage[self.index]:
            return False
        else:
            self.index+=1
            # 先判断左子树
            if root.left is not None and root.left.val==voyage[self.index]:
                return self.traversal(root.left, voyage) and self.traversal(root.right, voyage)
            elif root.left is not None and root.left.val!=voyage[self.index]:
                # 需要反转一下当前的这个节点
                self.flipped.append(root.val)
                # 先遍历右子树再遍历左子树
                return self.traversal(root.right, voyage) and self.traversal(root.left, voyage)
            else: # root.left is None，则遍历右子树
                return self.traversal(root.right, voyage)  
            
        