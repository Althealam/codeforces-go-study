# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        nums_set = set(nums)
        pre = dummy_node
        while pre.next:
            if pre.next.val in nums_set:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy_node.next