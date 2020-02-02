class StackWithMax:
    def __init__(self):
        self.max_stack = [0]

    def push(self, element):
        self.max_stack.append(max(self.max_stack[-1], element))

    def pop(self):
        self.max_stack.pop()

    def max(self):
        return self.max_stack[-1]


def main():
    a = StackWithMax()

    n = int(input())

    for _ in range(n):
        command = str(input())
        if command == 'pop':
            a.pop()
        elif command == 'max':
            print(a.max())
        else:
            a.push(int(command.split()[1]))


if __name__ == '__main__':
    main()
