# 剑指offer NO.2 替换空格
class Solution:
    def replaceSpace(self, s):
        num_space = 0
        new_s = []
        for char in s:
            if char == ' ':
                num_space += 1
            new_s.append(char)
        new_s = new_s + ['='] * 2 * num_space
        s_i = len(s) - 1
        new_s_i = len(new_s) - 1
        while s_i >= 0 and s_i < new_s_i:
            if s[s_i] == ' ':
                new_s[new_s_i-2 : new_s_i+1] = ['%', '2', '0']
                new_s_i -= 3
            else:
                new_s[new_s_i] = s[s_i]
                new_s_i -=1
            s_i -= 1
        new_s = ''.join(new_s)
        return new_s
if __name__ == '__main__':
    s = ' wdad ed '
    solt = Solution()
    print(solt.replaceSpace(s))

# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         i = 0
#         while i < len(s):
#             if s[i] == ' ':
#                 s = s[:i] + '%20' + s[i+1:]
#             i += 1
#         return s
# if __name__ == '__main__':
#     s = ''
#     solt = Solution()
#     print(solt.replaceSpace(s))