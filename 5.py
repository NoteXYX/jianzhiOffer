# 中序序列二叉树的下一个节点
class TreeLinkNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution():
    def GetNext(self, node):
        p_next = None
        if node.right != None:
            p = node.right
            while p.left != None:
                p = p.left
            p_next = p
        elif node.next != None:
            p_c = node
            p_parent = node.next
            while p_parent != None and p_c == p_parent.right:
                p_c = p_parent
                p_parent = p_parent.next
            p_next = p_parent
        return p_next


