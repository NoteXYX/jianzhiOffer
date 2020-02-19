# 机器人的运动范围
class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [False] * rows * cols
        count = self.hasCore(threshold, rows, cols, 0, 0, visited)
        del visited
        return count
    def hasCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.hasCore(threshold, rows, cols, row-1, col, visited) \
            + self.hasCore(threshold, rows, cols, row+1, col, visited) \
            + self.hasCore(threshold, rows, cols, row, col-1, visited) \
            + self.hasCore(threshold, rows, cols, row, col+1, visited)
        return count
    def check(self, threshold, rows, cols, row, col, visited):
        if 0 <= row < rows and 0 <= col < cols \
                and self.getDigitSum(row) + self.getDigitSum(col) <= threshold \
                and not visited[row * cols + col]:
            return True
        else:
            return False
    def getDigitSum(self, number):
        mysum = 0
        while number > 0:
            mysum += number % 10
            number = number // 10
        return mysum
if __name__ == '__main__':
    s = Solution()
    threshold = 2
    rows = 5
    cols = 5
    print(s.movingCount(threshold, rows, cols))