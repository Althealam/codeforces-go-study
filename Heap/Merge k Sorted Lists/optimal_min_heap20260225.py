# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(klogk+nlogk)=O(nlogk)
# space: O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        min_heap = []
        cur = dummy_node

        # 保持小顶堆的大小为O(k)
        for i in range(len(lists)): # time: O(k) k=len(lists)
            if lists[i]: # put the first node from every links into min_heap
                heapq.heappush(min_heap, (lists[i].val, i, lists[i])) # time: O(logk)
        
        while min_heap: # time: O(n) (iterate al nodes and push all nodes from the min_heap)
            val, i, node = heapq.heappop(min_heap) # O(logk)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next)) # O(logk)
        
        return dummy_node.next

        