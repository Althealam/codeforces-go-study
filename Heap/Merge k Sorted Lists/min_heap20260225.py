# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(nlogn)
# space: O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # suppose n is the number of all nodes, m is the number of lists
        min_heap = [] # space: O(n)
        for l in lists: # time: O(m) m is the number of lists
            while l: # time: O(n) 
                min_heap.append(l.val)
                l = l.next
        heapq.heapify(min_heap) # time: O(n)

        dummy_node = ListNode()
        cur = dummy_node
        for i in range(len(min_heap)): # time: O(n)
            cur.next = ListNode(heapq.heappop(min_heap)) # time: O(logn)
            cur = cur.next
        return dummy_node.next