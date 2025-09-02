import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_start(arr):
    R, C = len(arr), len(arr[0])

    # 위/아래 행
    for j in range(C):
        if arr[0][j] == 2:
            return [0, j]
        if arr[R-1][j] == 2:
            return [R-1, j]

    # 왼/오른쪽 열
    for i in range(R):
        if arr[i][0] == 2:
            return [i, 0]
        if arr[i][C-1] == 2:
            return [i, C-1]

def dfs(cr, cc):
    global ans 

    if grid[cr][cc] == 3:
        ans = 1
        return 
    
    for i in  range(4): 
        nr, nc = cr + dr[i], cc + dc[i]
        if (0<=nr<N) and (0<=nc<N):

            if  grid[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc)
    visited[cr][cc] = False 

T = int(input().strip())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * (N) for _ in range(N)]

    ans = 0 
    # 여기서 시작 지점 받아옴 
    sr, sc = find_start(grid)
    visited[sr][sc] = True
    dfs(sr, sc)

    print(ans)