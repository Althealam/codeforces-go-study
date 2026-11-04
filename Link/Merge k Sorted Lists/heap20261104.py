# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 核心思想：由于每条链表已经有序了，所有剩余节点中的最小值，一定在某条链表的头部。因此可以把各个链表的第一个节点放入最小堆中，堆中始终保留每条未处理完的链表的一个候选节点，并且最多为K个节点
# 时间复杂度：假设总节点数为N，链表数为K 时间复杂度为O(NlogK)
# 空间复杂度：O(K)堆最多保存K个候选节点

# 为什么不直接把所有节点入堆：会浪费每条链表已经有序的条件，并且时间复杂度更高，为O(NlogN)
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy_node = ListNode()
        min_heap = []
        cur = dummy_node

        # 保持小顶堆的大小为O(k)
        for i in range(len(lists)): # time: O(logk)
            if lists[i]: # 把每个链表的第一个节点推入堆中
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap) # O(logk)
            cur.next = node
            cur = cur.next
            if node.next:
                # time: O(logk)
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy_node.next