import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c):

    # visited와 q 만들기 
    visited = [[-1] * M for _ in range(N)]
    q = deque()

    visited[start_r][start_c] = 0
    q.append((start_r, start_c))

    while q:
        r, c = q.popleft()

        # 종료 조건
        if r == N-1 and c == M-1:  
            return visited[r][c]


        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 체크 
            if 0 <= nr < N and 0 <= nc < M:
                if data[nr][nc] and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    
    # 도달할 수 없을 때 값 
    return -1

N, M = map(int, input().split())
data = [list(map(int, input().strip())) for _ in range(N)]

result = bfs(0, 0)
print(result)