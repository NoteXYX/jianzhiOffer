# 二进制中1的个数
class Solution:
    def NumberOf1_1(self, n):
        x = 1
        count = 0
        while x < 2**32:
            if n & x:
                count += 1
            x = x << 1
        return count
    def NumberOf1_2(self, n):
        count = 0
        while n >= -2**31 - 1 and n != 0:
            count += 1
            n = n & (n - 1)
        return count
if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1_2(-1))
