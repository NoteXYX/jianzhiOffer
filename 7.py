# 斐波那契数列
class Solution:
    def Fibonacci_1(self, n):   # 循环实现
        fnm1 = 1
        fnm2 = 0
        if n == 0:
            return fnm2
        elif n == 1:
            return fnm1
        else:
            for i in range(2, n+1):
                f = fnm1 + fnm2
                fnm2 = fnm1
                fnm1 = f
            return f
    def Fibonacci_2(self, N):   # 递归实现，超时
        def FibonacciRe(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return FibonacciRe(n-1) + FibonacciRe(n-2)
        return FibonacciRe(N)

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci_2(3))
