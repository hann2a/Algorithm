import sys

sys.stdin = open('input.txt', 'r')

def check_bracket_use(string):
    check_dict = {')': '(', '}':'{', ']': '['}
    stack = []

    for char in string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if len(stack) ==0:
                return -1
            
            stack_char = stack.pop()
            if check_dict[char] != stack_char:
                return -1
            
        else:
                continue
    
    if len(stack) == 0:
        return 1
    else:
        return -1
    
T = int(input())
for test_case in range(1, T+1):
    bracket_set = input().strip()
    result = check_bracket_use(bracket_set)
    print(f'#{test_case} {result}')