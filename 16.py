# 数值的整数次方
import sys
class Solution:
    def Power(self, base, exponent):
        if base == 0 and exponent < 0:
            raise Exception('Invalid input!')
        if base == 0:
            return 0
        newExponent = abs(exponent)
        res = self.powerCore(base, newExponent)
        if exponent < 0:
            res = 1 / res
        return res
    def powerCore(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.powerCore(base, exponent >> 1)
        res *= res
        if exponent & 0x1 == 1:
            res *= base
        return res
if __name__ == '__main__':
    s = Solution()
    line = sys.stdin.readline().strip()
    num = list(map(int, line.split()))
    print(s.Power(num[0], num[1]))