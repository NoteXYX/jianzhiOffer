# 删除链表中重复的节点
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
    def deleteSameNode(self, head):
        if head == None or head.next == None:
            return head
        preNode = None
        pNode = head
        while pNode:
            pNext = pNode.next
            needDelete = False
            if pNext and pNode.val == pNext.val:
                needDelete = True
            if not needDelete:
                preNode = pNode
                pNode = pNext
            else:
                toBeDeleted = pNode
                value = pNode.val
                while toBeDeleted and toBeDeleted.val == value:
                    pNode = toBeDeleted.next
                    del toBeDeleted
                    toBeDeleted = pNode
                if preNode == None:
                    head = pNode
                else:
                    preNode.next = pNode
        return head
if __name__ == '__main__':
    s = Solution()
    nodeHead = ListNode(1)
    nodeHead.createNode(nodeHead, 2)
    nodeHead.createNode(nodeHead, 3)
    nodeHead.createNode(nodeHead, 3)
    nodeHead = s.deleteSameNode(nodeHead)