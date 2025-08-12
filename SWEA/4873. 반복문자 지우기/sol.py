import sys

sys.stdin = open('input.txt')

def same_pang(string):
    stack = []

    for char in string: 
        if len(stack) != 0:          # 스택에 아무것도 없는 게 아니라면 
            if stack[-1] == char:    # 마지막 것과 비교해서 같으면 pop
                stack.pop()
            else:
                stack.append(char)   # 마지막이랑 같지 않으면 추가 
        else:                        # 스택에 아무것도 없다면 추가 
            stack.append(char) 
    
    return len(stack)                # 스택의 길이 구함 
            

T = int(input())
for test_case in range(1, T+1):
    line = input().strip()
    result = same_pang(line)
    print(f'#{test_case} {result}')