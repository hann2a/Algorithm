import sys 
from collections import deque 

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    dq = deque(numbers)

    count = 0 
    while count < M:
        dq.rotate(-1)
        count += 1

    print(f'#{t} {dq[0]}')