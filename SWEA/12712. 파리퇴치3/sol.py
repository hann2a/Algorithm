import sys
sys.stdin = open("input.txt", "r")
"""
N x N 배열 
M의 세기 
한 번에 잡을 수 있는 최대 파리수 


"""

# 상 하 좌 우 좌상 우상 좌하 우하 
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0 

    for r in range(N):
        for c in range(N):
            now_point = arr[r][c]
            # M-1 만큼 돌아서 더해야됨 
            # 상하 좌우 돌기
            # sum_fly : 상하좌우 더한 값 
            # diagonal_fly : 대각선들 더한 값
            sum_fly = arr[r][c]        # 중심을 먼저 더해두고
            diagonal_fly = arr[r][c]   
            for k in range(1, M):         #   → k를 1부터 돌린다
                for i in range(4):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k
                    if (0 <= nr < N) and (0 <= nc < N):
                        sum_fly += arr[nr][nc]
                for i in range(4, 8):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k 
                    if (0 <= nr < N) and (0 <= nc < N):
                        diagonal_fly += arr[nr][nc]
            max_fly = max(max_fly, sum_fly, diagonal_fly)

    print(f"#{test_case} {max_fly}")