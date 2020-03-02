# 反转链表
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
    def reverseList(self, head): # 非递归版
        if head is None or head.next is None:
            return head
        p_i = head.next
        p_j = head
        p_j.next = None
        while p_i:
            tmp = p_i.next
            p_i.next = p_j
            p_j = p_i
            p_i = tmp
        return p_j


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.creatNode(head, 2)
    head.creatNode(head, 3)
    print(s.reverseList(head))