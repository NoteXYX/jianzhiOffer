# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # def creat(self, head, x):
    #     while head.next != None:
    #         head = head.next
    #     head.next = ListNode(x)

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        point = listNode
        res = []
        while point != None:
            res.append(point.val)
            point = point.next
        res.reverse()
        return res

s = Solution()
listNode = ListNode(1)
listNode.creat(listNode, 2)
listNode.creat(listNode, 3)
print(s.printListFromTailToHead(listNode))
