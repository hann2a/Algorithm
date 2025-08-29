import sys
sys.stdin = open('input.txt', 'r')

# input 받기 
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(r, c):
    visited[r][c] = True

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)

island = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            island += 1
            dfs(i, j)

print(island)
