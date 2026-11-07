class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy_node = ListNode()
        pre = dummy_node
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next= cur2
                cur2 = cur2.next
            pre = pre.next

        if cur1:
            pre.next = cur1
            pre = pre.next
            cur1 = cur1.next
        if cur2:
            pre.next = cur2
            pre = pre.next
            cur2 = cur2.next
        return dummy_node.next