# 需要后驱节点的原因：递归反转只是反转前面n个节点，但是必须要将反转后的链表重新接回剩余部分
# 思路：
# 1. 递归反转n-1个节点
# 2. 当前节点反转
# 3. 接回剩余链表
def reverseN(head, n):
    # 第n+1个节点，用来反转后接回链表
    successor = None

    def helper(node, n):
        nonlocal successor # 只在函数内部使用

        if n==1:
            successor = node.next
            return node
        
        # 1->2->3->4 ==> 1->2<-3<-4
        # 递归反转后面的n-1个节点
        new_head = helper(node.next, n-1)

        # node = 1, node.next = 2, node.next.next = 1
        # 1->2<-3<-4 => 1<-2<-3<-4
        # 当前节点反转
        node.next.next = node

        # None<-1<-2<-3<-4
        # 接回剩余的链表
        node.next = successor
        return new_head
    return helper(head, n)