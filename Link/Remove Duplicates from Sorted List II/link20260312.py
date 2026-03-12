# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        prev = dummy_node # 当前检查节点的前面一个节点
        while prev.next and prev.next.next:
            if prev.next.val==prev.next.next.val:
                duplicate_val = prev.next.val
                # 删除所有等于duplicate_val的节点
                while prev.next and prev.next.val==duplicate_val:
                    prev.next = prev.next.next # 删除操作，跳过prev.next节点
            else:
                # 没有重复，向前移动
                prev = prev.next
        return dummy_node.next

                



        