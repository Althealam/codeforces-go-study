# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        while pre and pre.next:
            if pre.val == pre.next.val:
                delete_val = pre.val
                while pre.next and pre.next.val==delete_val:
                    pre.next = pre.next.next
            else:
                pre = pre.next
        return head
                