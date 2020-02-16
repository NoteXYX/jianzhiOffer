# 快速排序算法
import random
class Solution:
    def Swap(self, data, x, y):
        tmp = data[x]
        data[x] = data[y]
        data[y] = tmp
        return data
    def partition(self, data, length, start, end):
        if data==None or length<=0 or start<0 or end>=length:
            raise Exception('Invalid input!')
        index = random.randint(start, end)
        data = self.Swap(data, index, end)
        small = start - 1
        for i in range(start, end):
            if data[i] <= data[end]:
                small += 1
                if small != i:
                    data = self.Swap(data, i, small)
        index = small + 1
        data = self.Swap(data, index, end)
        return index
    def quickSort(self, data, length, start, end):
        if start == end:
            return
        index = self.partition(data, length, start, end)
        if index > start:
            self.quickSort(data, length, start, index-1)
        if index < end:
            self.quickSort(data, length, index+1, end)
if __name__ == '__main__':
    s = Solution()
    data = [3,5,1,7,4,8,6,2]
    print(data)
    s.quickSort(data, len(data), 0, len(data)-1)
    print(data)
