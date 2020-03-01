# 正则表达式匹配
import sys
class Solution:
    def match(self, mystr, pattern):
        if mystr is None or pattern is None:
            return False
        return self.matchCore(mystr, pattern)
    def matchCore(self, mystr, pattern):
        if len(mystr) == 0 and len(pattern) == 0:
            return True
        if len(mystr) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if mystr and (pattern[0] == mystr[0] or pattern[0] == '.' ):
                return self.matchCore(mystr[1:], pattern[2:]) \
                       or self.matchCore(mystr[1:], pattern) \
                       or self.matchCore(mystr, pattern[2:])
            else:
                return self.matchCore(mystr, pattern[2:])
        if mystr and (pattern[0] == mystr[0] or pattern[0] == '.'):
            return self.matchCore(mystr[1:], pattern[1:])
        return False
if __name__ == '__main__':
    s = Solution()
    mystr = sys.stdin.readline().strip()
    pattern = sys.stdin.readline().strip()
    print(s.match(mystr, pattern))