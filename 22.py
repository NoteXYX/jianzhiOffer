# 链表的倒数第k个节点
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def creatNode(self, head, val):
        p = head
        while not p.next is None:
           p = p.next
        p.next = ListNode(val)
class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        p_i = head
        count = 0
        while p_i and count < k-1 :
            p_i = p_i.next
            count += 1
        if p_i is None:
            return None
        p_j = head
        while p_i.next:
            p_i = p_i.next
            p_j = p_j.next
        return p_j
if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.creatNode(head, 2)
    head.creatNode(head, 3)
    print(s.FindKthToTail(head, 4))