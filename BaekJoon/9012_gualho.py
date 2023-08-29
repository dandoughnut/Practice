n = int(input())

for i in range(n):
    line = input()
    stack = []
    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                # if there is no opening paranthesis:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')