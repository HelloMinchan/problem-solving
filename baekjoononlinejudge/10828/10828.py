import sys

input = sys.stdin.readline


class Stack(list):
    
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        return 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]


s = Stack()

for t in range(int(input())):
    c = input().rstrip().split(' ')
    if c[0] == 'push': s.push(c[1])
    elif c[0] == 'pop': print(s.pop())
    elif c[0] == 'size': print(s.size())
    elif c[0] == 'empty': print(s.isEmpty())
    else: print(s.top())