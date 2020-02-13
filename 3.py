# 从尾至头打印链表
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
    def create(self, p, v):
        while p.next != None:
            p = p.next
        p.next = ListNode(v)
# 递归实现
class recurSolution:
    def printListFromTailToHead(self, listNode):
        res = []
        def printListnode(listNode):
            if listNode:
                printListnode(listNode.next)  # 先递归到最后一层
                res.append(listNode.val)  # 添加值，退出函数，返回到上一层函数中的这行，继续添加值

        printListnode(listNode)
        return res

# 栈实现
class stackSolution:
    def printListFromTailToHead(self, listNode):
        chain = []
        res = []
        p = listNode
        while p != None:
            chain.append(p.val)
            p = p.next
        while len(chain) != 0:
            res.append(chain.pop())
        return res

if __name__ == '__main__':
    recur_s = recurSolution()
    stack_s = stackSolution()
    head = ListNode(1)
    head.create(head, 2)
    head.create(head, 3)
    print(recur_s.printListFromTailToHead(head))
    print(stack_s.printListFromTailToHead(head))

