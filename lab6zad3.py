def balanced_symbols(expression):
    stack = []
    opening_symbols = ['(', '[', '{', '<']
    closing_symbols = [')', ']', '}', '>']
    symbols_map = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for char in expression:
        if char in opening_symbols:
            stack.append(char)
        elif char in closing_symbols:
            if len(stack) == 0:
                return False
            last_opening_symbol = stack.pop()
            if not matching_symbol(last_opening_symbol, char, symbols_map):
                return False

    return len(stack) == 0

def matching_symbol(opening_symbol, closing_symbol, symbols_map):
    return symbols_map[opening_symbol] == closing_symbol


expression1 = "(())"
expression2 = "{[<>]}"
expression3 = "[{()]"
expression4 = "<>[]{}"

print(balanced_symbols(expression1))  #True
print(balanced_symbols(expression2))  #True
print(balanced_symbols(expression3))  #False
print(balanced_symbols(expression4))  #True
