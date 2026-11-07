# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy_node = ListNode(next=head)
        pre = dummy_node
        while pre.next and pre.next.next:
            if pre.next.val==pre.next.next.val:
                duplicate_val = pre.next.val
                while pre.next and pre.next.val==duplicate_val:
                    pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy_node.next

