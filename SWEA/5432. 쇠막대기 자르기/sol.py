import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())

    # 괄호가 레이저를 만들거나 혹은 닫힐 때까지 저장하는 스택 
    stack = []

    # count_st : 스택에 몇 개가 담겼는지 
    # count_sl : 지금까지 조각이 몇 개였는지 
    count_st = 0 
    count_sl = 0
    
    # prev : 직전 괄호를 저장하는 변수 | 시작 초기화 
    prev = ''

    # bckt : 괄호 하나 
    for bckt in arr:
        # 괄호가 '(' 이면 스택에 담고 수를 센다 
        if bckt == '(':
            stack.append(bckt)
            count_st += 1

        # 괄호가 ')'이면 기존의 '('을 스택에서 나오게 한다 (pop)
        # 나왔으므로 스택의 개수를 하나 뺀다 
        else:
            stack.pop()
            count_st -= 1

            # 만약 직전 괄호가 '('이면 레이저라는 뜻이므로 
            # 지금까지 모아놓은 스택만큼 슬라이스가 생긴다
            if prev == '(':
                count_sl += count_st
            
            # 직전 괄호가 ')' 이라면 이번 괄호도 닫힌 것이므로 
            # 조각 하나를 추가한다
            else:
                count_sl += 1
        # 하나의 괄호로 모든 계산을 끝냈으므로 직전 변수에 저장한다
        prev = bckt 

    print(f"#{test_case} {count_sl}")