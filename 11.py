# 旋转数组中的最小数字
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray==None or len(rotateArray)==0:
            raise Exception('Invalid input')
        indexMid = 0
        index1 = indexMid
        index2 = len(rotateArray)-1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2
            if rotateArray[index1] == rotateArray[index2] == rotateArray[indexMid]:
                return self.orderIn(rotateArray, index1, index2)
            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid
            if rotateArray[indexMid] <= rotateArray[index2]:
                index2 = indexMid
        return rotateArray[indexMid]
    def orderIn(self, array, index1, index2):
        res = array[index1]
        for i in range(index1+1, index2+1):
            if array[i] < res:
                res = array[i]
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([1,1,1,0,1]))