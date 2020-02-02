import math


class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, element):
        if self.stack:
            self.stack.append((element, max(element, self.stack[-1][1])))
        else:
            self.stack.append((element, element))

    def pop(self):
        return self.stack.pop()[0]

    def get_max(self):
        if not self.stack:
            return -math.inf
        return self.stack[-1][1]


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, elem):
        self.s1.push(elem)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def get_max(self):
        return max(self.s1.get_max(), self.s2.get_max())


def main():
    a = Queue()
    a.push(2)
    a.push(7)
    a.push(3)
    a.push(1)
    print(a.get_max())
    a.push(5)
    a.pop()
    print(a.get_max())
    a.push(2)
    a.pop()
    print(a.get_max())
    a.push(6)
    a.pop()
    print(a.get_max())
    a.push(2)
    a.pop()
    print(a.get_max())

if __name__ == '__main__':
    main()
