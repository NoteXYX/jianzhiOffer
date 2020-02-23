# 剪绳子
class Solution:
    # 动态规划
    def cutRope1(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        products = {}
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, number+1):
            max = 0
            for j in range(1, i // 2 + 1):
                p = products[j] * products[i-j]
                if p > max:
                    max = p
            products[i] = max
        max = products[number]
        del products
        return max
    # 贪心算法
    def cutRope2(self, number):
        if number == 1:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        timesOf3 = number // 3
        if number - 3 * timesOf3 == 1:  # 如果最后剩下一段长度为4的绳子
            timesOf3 -= 1
        timesOf2 = (number - 3 * timesOf3) // 2
        return pow(3, timesOf3) * pow(2, timesOf2)
if __name__ == '__main__':
    s = Solution()
    print(s.cutRope2(8))