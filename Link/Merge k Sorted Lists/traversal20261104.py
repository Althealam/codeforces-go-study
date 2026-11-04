# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：把K条链表分成两半，分别合并，再把两个结果合并（分治思想）
# 时空复杂度：假设K是链表数量，N是所有链表的节点总数
# 合并两条链表：假设两条链表分别有a、b个节点 -> 时间为O(a+b)，空间为O(1)
# 分治：O(Nlogk)，递归深度为K，最多每层处理N个节点，因此为Nlogk；递归同样有空间复杂度，为O(logK)
# 总结：时间复杂度为O(Nlogk)，空间复杂度为O(logK)
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        m = len(lists)
        if m==0:
            return None
        if m==1:
            return lists[0]
        left = self.mergeKLists(lists[:m//2]) # 合并左半部分
        right = self.mergeKLists(lists[m//2:]) # 合并右半部分
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2 
                list2 = list2.next

            cur = cur.next
        cur.next = list1 if list1 else list2 # 拼接剩余链表
        return dummy.next