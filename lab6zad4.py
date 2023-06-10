def evaluate_rpn(expression):
    stack = []

    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack.pop()


expression = ['6', '1', '3', '-', '+', '7', '*']
result = evaluate_rpn(expression)
print(result)
