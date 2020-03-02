# 表示数字的字符串
import sys
class Solution:
    def isNumeric(self, s):
        if s is None or s == '':
            return False
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, ch in enumerate(s):
            if ch in ['+', '-']:
                if i > 0 and (s[i-1] not in ['e', 'E']):
                    return False
            elif ch == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif ch in ['e', 'E']:
                if met_e or (not met_digit):
                    return False
                met_e = True
                met_digit = False
            elif ch.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    s = Solution()
    print(s.isNumeric(line))