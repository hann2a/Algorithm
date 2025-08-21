import sys
from itertools import permutations

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')

    # n-1까지의 열 인덱스 생성 
    cols = list(range(N))

    # 열 인덱스로 만들 수 있는 식, 제너레이터 
    for p in permutations(cols):
        
        sum_c = 0
        # 현재 순열(p)에 따라 합계를 계산
        for r in range(N):
            c = p[r]
            sum_c += arr[r][c]
            # 모든 열 순회를 막기 위해 최소합보다 커지면 브레이크
            if sum_c > min_sum:
                break

        # 계산된 합계가 기존 최솟값보다 작으면 갱신
        min_sum = min(min_sum, sum_c)

    print(f'#{tc} {min_sum}')
