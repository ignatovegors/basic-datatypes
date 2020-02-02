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


def main():
    a = Stack()

    n = int(input())

    for _ in range(n):
        command = str(input())
        if command == 'pop':
            a.pop()
        elif command == 'max':
            print(a.get_max())
        else:
            a.push(int(command.split()[1]))


if __name__ == '__main__':
    main()
