import sys
from collections import deque 
sys.stdin = open('input.txt', 'r')

T = 10 

for t in range(1, T+1):
    num = int(input())
    data = list(map(int, input().split()))

    # 프로그램 종료 조건 : 하나라도 0 이 된다 
    # 0보다 작아질 수는 없다 
    dq = deque(data)

    Flag = True
    while Flag:
        for i in range(1, 6):
            dq[0] -= i
            if dq[0] <= 0:
                # 0을 지나쳐서 음수가 바로 되어버릴 수 있음 
                dq[0] = 0 
                dq.rotate(-1)
                Flag = False
                break 
            else:
                dq.rotate(-1)

    print(f'#{t}', *dq)