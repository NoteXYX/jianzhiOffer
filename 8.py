# 跳台阶 1 or 2
class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        fnm1 = 2
        fnm2 = 1
        for i in range(3, number+1):
            f = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = f
        return f
if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(3))