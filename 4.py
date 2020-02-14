# 给定前序和中序遍历，重建二叉树
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        def ConstructCore(startPre, endPre, startIn, endIn):
            rootVal = pre[startPre]
            root = treeNode(rootVal)
            if startPre == endPre:
                if startIn == endIn and pre[startPre] == tin[startIn]:
                    return root
                else:
                    print('Invalid input.')
            # 在中序遍历中找到根结点
            rootIn = startIn
            while rootIn < endIn and tin[rootIn] != rootVal:
                rootIn += 1
            if rootIn == endIn and tin[rootIn] != rootVal:
                print('Invalid input.')
            leftLength = rootIn - startIn
            leftPreEnd = startPre + leftLength
            if leftLength > 0: # 若左子树不为空，构建左子树
                root.left = ConstructCore(startPre+1, leftPreEnd, startIn, rootIn-1)
            if leftLength < endIn - startIn: # 若右子树不为空，则构建右子树
                root.right = ConstructCore(leftPreEnd+1, endPre, rootIn+1, endIn)
            return root

        assert len(pre) == len(tin)
        if pre == None or tin == None or len(pre) == 0:
            return None
        else:
            return ConstructCore(0, len(pre)-1, 0, len(tin)-1)


if __name__ == '__main__':
    s = Solution()
    # pre = [1,2,3,4,5,6,7]
    # tin = [3,2,4,1,6,5,7]
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    print(s.reConstructBinaryTree(pre, tin).val)