# 从尾至头打印链表
# 递归法
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
    def create(self, p, v):
        while p.next != None:
            p = p.next
        p.next = ListNode(v)

class Solution:
    def printListFromTailToHead(self, listNode):
        res = []
        def printListnode(listNode):
            if listNode:
                printListnode(listNode.next)  # 先递归到最后一层
                res.append(listNode.val)  # 添加值，退出函数，返回到上一层函数中的这行，继续添加值

        printListnode(listNode)
        return res

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.create(head, 2)
    head.create(head, 3)
    print(s.printListFromTailToHead(head))

