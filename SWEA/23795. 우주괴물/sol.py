import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 괴물 찾기 

    mon_r, mon_c = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                mon_r, mon_c = r, c
                break 
    
    # 광선 위치 표시 visited
    visited = [[False] * N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for direct in range(4):
        nr, nc = mon_r + dr[direct], mon_c + dc[direct]

        # 경계를 벗어나지 않고 벽에 막히지 않는 동안 계속 
        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
            visited[nr][nc] = True 

            nr += dr[direct]
            nc += dc[direct]

    not_light = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0 and not visited[r][c]:
                not_light += 1

    print(f'#{t} {not_light}')