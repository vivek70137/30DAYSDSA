'''
stack = []
pairs = {')': '(', '}': '{', ']': '['}
s = 'as[]'

for char in s:
    if char in pairs.values():
        stack.append(char)
    elif char in pairs:
        if not stack or stack.pop() != pairs[char]:
            print('False')
            break
else:
    # If the loop completes without breaking, check if the stack is empty
    if not stack:
        print('True')
    else:
        print('False')'''

s='as[]'
if len(s) % 2 == 1:
        print(' False')

stack = []
for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if len(stack) == 0:
                print( 'False')
            c = stack.pop()
            if not ((c == '(' and char == ')') or 
                    (c == '{' and char == '}') or 
                    (c == '[' and char == ']')):
                print('False')


    
