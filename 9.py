# 变态跳台阶 1 or 2 or...or n
class Solution:
    def jumpFloorII(self, number):
        return 2 ** (number-1)
if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(3))