import sys

sys.stdin = open('input.txt', 'r')

from collections import deque
# N X M의 모눈종이 
# 2변 이상이 공기와 닿으면 녹음 
# 바깥 공기와 내부 공기를 어떻게 구분하지 

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 전체를 순회하면서 해당 치즈가 두 면 이상 바깥과 접촉했는지 확인후 그렇다면 
# 해당 치즈는 다음에 없앰 

# Q. 이게 진짜 바깥인지 어케 알음? 
# ->> 아하... 바깥부터 시작하는구나
# >> 바깥에서 bfs를 쓰면 기존 바깥의 연결공간만 계속해서 확인할 수 있기 때문에
# 바깥에서 만난 치즈만 녹일 수 있게 됨 

cheese = 0 
# 치즈 개수 미리 세기 
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese += 1 
def bfs():
    # (0, 0)부터 시작 
    q = deque([(0, 0)])
    # 방문 배열 초기화 
    visited = [[0] * M for _ in range(N)]
    # 방문 표시 
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                
                elif arr[nr][nc] == 1:
                    visited[nr][nc] += 1

    count_cheese = 0 
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] >= 2:
                # 녹이기
                arr[i][j] = 0 
                count_cheese += 1

    return count_cheese

hour = 0 
while cheese > 0:
    melted = bfs()
    cheese -= melted
    hour += 1

print(hour)