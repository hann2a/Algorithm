import sys

sys.stdin = open('input.txt')

"""
맞으면 1 아니면 0 
"""
def check_bracket(string):
    check_dict = {'}':'{', ')':'('}
    stack = []

    for char in string:
        if char in '({':
            stack.append(char)

        elif char in ')}':
            if len(stack) == 0:
                return 0
            
            stack_char = stack.pop()
            if check_dict[char] != stack_char:
                return 0
        else:
            continue 
    
    if len(stack) !=0:
        return 0
    else:
        return 1
    
T = int(input())
for test_case in range(1, T+1):
    line = input().strip()
    result = check_bracket(line)
    print(f'#{test_case} {result}')