# 打印从1到最大的n位数
import sys
class Solution:
    def printNumbers(self, n):
        tar = 10 ** n - 1
        for i in range(1, tar+1):
            print(i)
if __name__ == '__main__':
    s = Solution()
    n = int(sys.stdin.readline().strip())
    s.printNumbers(n)