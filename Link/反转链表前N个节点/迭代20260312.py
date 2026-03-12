# 1->2->3->4, n=2
# 2->1->3->4, return 2
def reverseN(head, n):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    nxt = head.next
    while n>0:
        # 1->2->3->4 ==> None<-1 2->3->4 (pre = 1, cur=2, nxt = 3, n = 1)
        # None<-1 2->3->4 ==> None<-1<-2 3->4 (pre = 2, cur = 3, nxt = 4, n = 0)
        cur.next = pre
        pre = cur
        cur = nxt
        if nxt is not None:
            nxt = nxt.next
        n-=1
        
    # pre = 2, cur = 3, nxt = 4
    head.next = cur
    return pre


    
