# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(n)
class Solution:
    # 输入一个节点head，将以head为起点的链表反转，并返回反转后的头节点
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 1->2->3->4 ==> 1->2<-3<-4 (last)
        last = self.reverseList(head.next) # 反转head后面的链表
        # head.next = 2, head.next.next=1
        # head.next.next = head => 1<-2<-3<-4
        head.next.next = head
        # None<-1<-2<-3<-4
        head.next = None
        return last
