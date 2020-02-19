# 矩阵中的路径
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            raise Exception('Invalid input!')
        visited = [0] * (rows * cols)
        pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasCore(matrix, rows, cols, i, j, visited, path, pathLength):
                    return True
        del visited
        return False
    def hasCore(self, matrix, rows, cols, row, col, visited, path, pathLength):
        if pathLength == len(path):
            return True
        hasC = False
        if 0 <= row < rows and 0 <= col < cols and not visited[row * cols + col] and matrix[row * cols + col] == path[pathLength]:
            pathLength += 1
            visited[row * cols + col] = True
            hasC = self.hasCore(matrix, rows, cols, row-1, col, visited, path, pathLength) \
            or self.hasCore(matrix, rows, cols, row+1, col, visited, path, pathLength) \
            or self.hasCore(matrix, rows, cols, row, col-1, visited, path, pathLength) \
            or self.hasCore(matrix, rows, cols, row, col+1, visited, path, pathLength)
            if not hasC:
                pathLength -= 1
                visited[row * cols + col] = False
        return hasC
if __name__ == '__main__':
    s = Solution()
    rows = 3
    cols = 4
    matrix = 'A A A A A A A A A A A A'.split()
    path = 'AAAAAAAAAAAA'
    print(s.hasPath(matrix, rows, cols, path))