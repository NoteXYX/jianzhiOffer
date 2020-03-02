# 调整数组顺序使奇数位于偶数前面
import sys
class Solution:
    def reOrderArray(self, array):  # 相邻双指针
        if array == [] or len(array) == 1:
            return array
        i = 0
        j = 0
        while i < len(array) and j < len(array):
            while i < len(array) and array[i] & 1 != 0: # 若为奇数
                i += 1
            j = i + 1
            while j < len(array) and array[j] & 1 == 0: # 若为偶数
                j += 1
            if j < len(array):
                tmp_index = j
                tmp = array[j]
                while j > i:
                    array[j] = array[j-1]
                    j -= 1
                array[i] = tmp
                j = tmp_index
        return array
    # def reOrderArray(self, array): # 头尾双指针法不稳定，但时间复杂度低
    #     if array == []:
    #         return []
    #     begin = 0
    #     end = len(array) - 1
    #     while begin < end:
    #         while array[begin] & 0x1 != 0 and begin < end:
    #             begin += 1
    #         while array[end] & 0x1 == 0 and end > begin:
    #             end -= 1
    #         if begin < end:
    #             tmp = array[begin]
    #             array[begin] = array[end]
    #             array[end] = tmp
    #             begin += 1
    #             end -= 1
    #     return array
if __name__ == '__main__':
    s = Solution()
    line = sys.stdin.readline().strip()
    array = list(map(int, line.split()))
    print(s.reOrderArray(array))
