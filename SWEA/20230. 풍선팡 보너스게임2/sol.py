import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0
    for r in range(N):
        for c in range(N):
            sum_r = sum(arr[r])
            sum_c = 0
            for i in range(N):
                sum_c += arr[i][c]
            
            result = sum_r + sum_c - arr[r][c]

            if max_result < result:
                max_result = result
    
    print(f'#{t} {max_result}')