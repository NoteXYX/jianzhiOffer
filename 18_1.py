# 删除链表的节点
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def createNode(self, nodeP, val):
        curNode = ListNode(val)
        while nodeP.next != None:
            nodeP = nodeP.next
        nodeP.next = curNode
class Solution:
    def deleteNode(self, nodeP, nodeN):
        if nodeN.next == None:
            p = nodeP
            while p.next != nodeN:
                p = p.next
            p.next = None
            del nodeN
            return nodeP
        elif nodeP.next == None:
            return None
        else:
            nodeN.val = nodeN.next.val
            nodeN.next = nodeN.next.next
            return nodeP
if __name__ == '__main__':
    s = Solution()
    nodeHead = ListNode(1)
    nodeHead.createNode(nodeHead, 2)
    nodeHead.createNode(nodeHead, 3)
    nodeHead.createNode(nodeHead, 4)
    nodeP = s.deleteNode(nodeHead, nodeHead)