def reverseN(self, head, n):
    # 在这段代码里，实现了如何将反转后的链表和后面的部分拼接在一起
    # 1->2->3->4->5, n=2 ==> 2->1->3->4->5

    pre = None
    cur = head
    while n>0:
        nxt =cur.next  # pre=None, cur=1, nxt=2; pre=1, cur=2, nxt=3
        cur.next = pre # None<-1 2->3->4->5; None<-1<-2 3->4->5
        pre = cur # pre=1, cur=2; pre=2, cur=3
        cur = nxt 
        n-=1
    head.next = cur # head=1, head.next = None, cur=3 ==> 2->1->3->4->5
    return pre