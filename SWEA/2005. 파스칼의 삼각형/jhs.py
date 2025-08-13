"""
stack : 양옆에 0이 패딩된 현재 스택. while문을 반목하면서 다음 층을 생성할때 사용됨.
next_stack : 다음 층의 스택을 갱신해주기 위한 준비단계에서 사용되는 스택

next_stack = [0]
next_stack .append(0)
를 통해 next_stack역시 양옆에 0 패딩을 진행.

 while문은 stack에 값이 1보다 크면 반목
next_stack을 만들어가는 구조   /     결괏값 print를 분리하여 진행

right : stack에 인덱스 [-1]의값이 pop됨
left : .stack에 인덱스 [-2]의 값이 pop됨

next_stack에 right와 left를 더한 값을 추가.    /     left와 right이 더해진값을 바로 print 해줌.
-> next_stack은 [0, 1, 1] 인상태일때        /     '1 1' 이 print되고 있는 상황  

while문이 종료되서 next_stack이 다 추가되었으면
0을 append해서 오른쪽에 패딩을 마무리해주고
stack을 갱신.
"""


import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 미리 테스트 번호 출력 
    print(f'#{t}')
    # 첫 번째 줄은 항상 1이므로 출력 
    print(1)
    # 첫 번째 줄의 상황을 stack에 넣어놓는다. (단, 양 옆에 0으로 패딩을 추가)
    stack = [0, 1, 0]

    # 두 번째 줄부터 포문 돌기 
    for i in range(1, N):
        # stack을 재 할당하기 위한 result 스택 초기화 
        result = [0]
        # 만약 스택의 길이가 1이상이면 반복 
        while len(stack) > 1:
            right = stack.pop()
            left = stack.pop()
            result.append(left + right)
            print(left + right, end=' ')
            # left는 재활용되어야 하므로 다시 append 해준다 
            stack.append(left)
        print()
        # 마지막으로 0패딩을 해주고
        result.append(0)
        # stack을 다음 단계로 설정해준다
        stack = result 