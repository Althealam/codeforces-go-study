def reverseN(head, n):
    if n==1:
        return head, head.next
    new_head, successor = reverseN(head.next, n-1)
    head.next.next = head
    head.next = successor
    return new_head, successor

new_head, _ = reverseN(head, n)