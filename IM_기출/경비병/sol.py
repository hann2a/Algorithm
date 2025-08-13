import sys

sys.stdin = open('input.txt')

"""
상하좌우로 n만큼 관찰 
공간 0 기둥 1 경비병 2 
"""


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 경비병 찾기 

    mon_r, mon_c = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                mon_r, mon_c = r, c
                break 
    
    # 경비병 볼 수 있는 위치 표시 visited
    visited = [[False] * N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for direct in range(4):
        nr, nc = mon_r + dr[direct], mon_c + dc[direct]
        # 거리 N을 넘어가는 건 제외 
        steps = 1    
        
        # 경계를 벗어나지 않고 벽에 막히지 않고 N보다 적은 거리인 동안 계속 
        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and steps <= N:
                visited[nr][nc] = True 

                nr += dr[direct]
                nc += dc[direct]
            

    not_visible = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0 and not visited[r][c]:
                not_visible += 1

    print(f'#{t} {not_visible}')