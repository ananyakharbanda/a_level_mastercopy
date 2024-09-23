

def precedence(element):
    if element in '*/':
        return 2
    elif element in '+-':
        return 1
    else:
        return 0

def infixtopostfix(infixString):
    infix = infixString.replace(' ', '')
    n = len(infix)
    output = []
    stack = []

    for i in range(n):
        if infix[i].isalnum():
            output.append(infix[i])

        elif infix[i] == '(':
            stack.append('(')
        
        elif infix[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        
        elif infix[i] in '+/-*':
            while stack and precedence(stack[-1]) >= precedence(infix[i]):
                output.append(stack.pop())
            stack.append(infix[i])
        
    while stack:
        if stack[-1] not in '()':
            output.append(stack.pop())
        else:
            stack.pop()
    print(' '.join(output))

infixtopostfix('A * (B + C) - D / E')
        
