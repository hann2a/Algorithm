import sys

sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return (i, j)
            
def find_end(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return (i, j)

def dfs(r, c, depth):
    global best 

    if r == er and c == ec:
        if best > depth -1:
            best = depth -1 
            return 
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, depth+1)
                visited[nr][nc] = False 
  
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 시작 지점 찾아서 할당 
    sr, sc = find_start(arr)
    # print(sr, sc)

    # 종료 지점 찾아서 할당 
    er, ec = find_end(arr)
    # print(er, ec)

    visited = [[False] * (N) for _ in range(N)]
    visited[sr][sc] = True

    best = float('inf')

    dfs(sr, sc, 0)

    result_min = 0 if best == float('inf') else best

    print(f'#{t} {result_min}')