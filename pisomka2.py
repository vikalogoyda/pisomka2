def to_infix(postfix_expr):
    stack = []
    for token in postfix_expr.split():
        if token.isdigit():
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()
            new_expr = f"( {left} {token} {right} )" 
            stack.append(new_expr)
    return stack[0]

print(to_infix("1 2 *"))
print(to_infix("1 2 * 3 +"))    
print( to_infix("1 2 3 * +"))  
print( to_infix("1"))     


def to_postfix(infix_expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    
    for token in infix_expr.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)



print(to_postfix("1"))
print(to_postfix("( 1 + 2 )"))
print(to_postfix("( 10 * ( 1 + 2 ) )"))
print(to_postfix("( ( 10 + 1 ) * ( 2 / 3 ) )"))
     