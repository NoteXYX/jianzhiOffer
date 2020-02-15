from queue import Queue
# 利用两个栈实现队列
class Solution1:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            print('queue is empty!')
        else:
            return self.stack2.pop()
# 两个队列实现栈
class Solution2:
    def __init__(self):
        self.q1 = Queue(maxsize=0)
        self.q2 = Queue(maxsize=0)
    def push(self, node):
        if not self.q1.empty():
            self.q1.put(node)
        elif not self.q2.empty():
            self.q2.put(node)
        else:
            self.q1.put(node)
    def pop(self):
        if not self.q1.empty():
            while self.q1.qsize() > 1:
                self.q2.put(self.q1.get())
            return self.q1.get()
        elif not self.q2.empty():
            while self.q2.qsize() > 1:
                self.q1.put(self.q2.get())
            return self.q2.get()
        else:
            print('stack empty')
if __name__ == '__main__':
    s = Solution2()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()