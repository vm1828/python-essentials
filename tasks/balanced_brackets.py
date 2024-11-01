def is_balanced(s):
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for char in s:
        # if char not in openers+closers:
        #     continue
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if stack == [] or brackets[stack[-1]] != char:
                return False
            stack.pop()
    return True if len(stack) == 0 else False

# def is_balanced(s):
#     stack = []
#     openers = ['(', '[', '{']
#     closers = [')', ']', '}']
#     for char in s:
#         # if char not in openers+closers:
#         #     continue
#         if char in openers:
#             stack.append(char)
#         elif char in closers:
#             if stack == [] or openers.index(stack[-1]) != closers.index(char):
#                 return False
#             stack.pop()
#     return True if len(stack) == 0 else False
