# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下

# 2. DFS三部曲
#（1）返回值含义：return True/False，如果是True则表示以当前node为根节点的子树种找到了一个subpath，这个subpath和link是一样的
#（2）终止条件：如果node为空，则说明这棵树找完了也没找到起点，返回False
#（3）携带信息：链表的头节点
#（4）单层递归的逻辑
# - 接收结果
#   - res_self = 调用匹配函数，看看从当前节点开始能不能匹配成功
#   - res_left：递归调用，从左子树里找起点
#   - res_right：递归调用，从右子树里找起点
# - 逻辑加工：无
# - 最终汇总：or（只要自己是起点或者左子树有起点或者右子树有起点）

# 3. 辅助递归
#（1）任务类型：自顶向下
#（2）DFS三部曲
#（2.1）返回值含义：表示从当前位置开始，剩下的路径是否能完美匹配剩下的链表
#（2.2）携带信息：当前应该匹配的链表节点list_node
#（2.3）终止条件
# - 如果list_node为空，说明链表已经遍历完毕，则直接返回True
# - 如果树节点为空，说明路径断了，返回False
# - 判断值：如果root.val!=list_node.val，则返回False
#（2.4）单层递归的逻辑
# - check_left用左子树去匹配链表的下一个节点
# - check_right用右子树去匹配链表的下一个节点
# - 最终汇总：or

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(head, root)
    
    def dfs(self, head, node):
        if node is None:
            return False
        if self.ismatch(head, node):
            return True
        return self.dfs(head, node.left) or self.dfs(head, node.right)
    
    def ismatch(self, head, node):
        if head is None:
            return True
        if node is None:
            return False
        if node.val!=head.val:
            return False
        return self.ismatch(head.next, node.left) or self.ismatch(head.next, node.right)

        