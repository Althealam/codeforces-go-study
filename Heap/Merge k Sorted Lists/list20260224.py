# Definition for singly-linked list.
# 假设K是链表的总个数，N是所有链表中的节点总数，链表的平均长度是L=N/K
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if n==0:
            return []
        elif n==1:
            return lists[0]
        mid = n//2
        left = self.mergeTwoLists(lists[:mid]) 
        right = self.mergeTwoLists(lists[mid:])
        # time: O(Nlogk)
        # total number of levels: O(logk)
        # total number of nodes for each level: O(N)
        # space: O(logk)
        return self.mergeKLists(left, right)
    
    def mergeTwoLists(self, list1, list2):
        # time: O(n1+n2), n1=len(list1), n2=len(list2)
        # space: O(1)
        dummy_node = ListNode()
        cur = dummy_node
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            elif list1.val>=list2.val:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1!=None:
            cur.next = list1
            list1 = list1.next
        elif list2!=None:
            cur.next = list2
            list2 = list2.next
        return dummy_node.next

def linked_list(list):
    if len(list)==0:
        return None
    dummy = ListNode()
    cur = dummy
    for i in range(len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return dummy.next

def print_list(list):
    res = []
    cur = list
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)
    return res

sol = Solution()
# list1 = linked_list([1, 4, 5])
# list2 = linked_list([1, 3, 4])
# list3 = linked_list([2, 6])
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merge = sol.mergeKLists(lists)
print_list(merge)