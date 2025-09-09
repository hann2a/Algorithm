import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

T = int(input())

# 탈주범이 위치할 수 있는 장소의 개수를 계산

tunnels = { # 상 하 좌 우
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

opposite = {0:1, 1:0, 2:3, 3:2}

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1

    while q:
        cr, cc = q.popleft()
        direction = tunnels[under_map[cr][cc]]

        for dir in range(4):
            if direction[dir] == 0:
                continue

            nc = cc + dc[dir]
            nr = cr + dr[dir]

            # 범위 밖이면 pass
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 못 가는 곳이면 pass
            if under_map[nr][nc] == 0:
                continue

            # 이미 방문했으면
            if visited[nr][nc]:
                continue

            n_direction = tunnels[under_map[nr][nc]]
            if n_direction[opposite[dir]] == 0:
                continue

            if visited[cr][cc] + 1 > time:
                continue

            visited[nr][nc] = visited[cr][cc] + 1
            q.append((nr, nc))



for t in range(1, T+1):
    N, M, sr, sc, time = map(int, input().split())
    under_map = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    bfs(sr, sc)
    count = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= time:
                count += 1

    print(f'#{t} {count}')
