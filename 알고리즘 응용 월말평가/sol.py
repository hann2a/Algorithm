import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0 

    for r in range(N-M+1):
        for c in range(N-M+1):
            
            now_flies = 0 

            for i in range(r, r+M):
                for j in range(c, c+M):
                    now_flies += arr[i][j]
            
            if max_flies < now_flies:
                max_flies = now_flies
    
    print(f'#{t} {max_flies}')

