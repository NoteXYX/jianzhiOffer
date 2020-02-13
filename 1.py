# 数组查找
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if target in array[i]:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    array = [[2,3,4],[3,4,5]]
    print(s.Find(5,array))