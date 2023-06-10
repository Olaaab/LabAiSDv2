def is_balanced(expression):
    stack = []
    opening_chars = ['(', '[', '{']
    closing_chars = [')', ']', '}']

    for char in expression:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if len(stack) == 0:
                return False
            last_opening_char = stack.pop()
            if not is_matching_chars(last_opening_char, char):
                return False

    return len(stack) == 0


def is_matching_chars(opening_char, closing_char):
    char_map = {'(': ')', '[': ']', '{': '}'}
    return char_map[opening_char] == closing_char


expression1 = "(()()()())"
expression2 = "(((())))"
expression3 = "(()((())()))"
expression4 = "((((((())"
expression5 = "()))"
expression6 = "(()()(()"

print(is_balanced(expression1))  # True
print(is_balanced(expression2))  # True
print(is_balanced(expression3))  # True
print(is_balanced(expression4))  # False
print(is_balanced(expression5))  # False
print(is_balanced(expression6))  # False
