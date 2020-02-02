def brackets(st):
    char_stack = []
    ind_stack = []
    op = ['(', '[', '{']
    cl = [')', ']', '}']
    counter = 1

    for element in st:
        if element in op:
            char_stack.append([element, counter])
            ind_stack.append(op.index(element))
        elif element in cl:
            if not ind_stack:
                return counter
            if cl.index(element) == ind_stack[-1]:
                ind_stack.pop()
                char_stack.pop()
            else:
                return counter
        counter += 1

    if char_stack:
        return char_stack[0][1]
    else:
        return 'Success'


def main():
    inp = str(input())

    print(brackets(inp))


if __name__ == '__main__':
    main()
