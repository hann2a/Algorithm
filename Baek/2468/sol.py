# 일정한 높이 이하의 모든 지점은 물에 잠김 
# 안전 영역 : 붙어있는 걸 하나로 치는 개수 

import sys

sys.stdin = open('input.txt', 'r')

from collections import deque 

N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

max_result = 1

# 비가 하나도 안오면 인접영역은 1이므로 1부터 시작해도 됨 
max_height = 0

for i in range(N):
    for j in range(N):
        if region[i][j] > max_height:
            max_height = region[i][j]

rain = 0 

# 비가 최대 높이보다 덜 오는 동안(최대 높이면 다 잠김)
while rain < max_height:

   # 방문 체크 
    visited = [[False] * N for _ in range(N)]
    # 카운트 초기화 | 이 비가 오는 것 기준 
    count = 0 

    for i in range(N):
        for j in range(N):

            # 만약 비 높이보다 region[i][j]가 크고 아직 방문하지 않았다면 
            if region[i][j] > rain and not visited[i][j]:
                
                # 세기 
                count += 1
                # 방문 체크 
                visited[i][j] = True 
                # 큐에 넣음 
                queue = deque([(i, j)])
                
                # 큐가 빌 때까지 반복 
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        # 만약 지도 안에 있고 
                        if 0 <= nr < N and 0 <= nc < N:
                            # 비보다 높고 아직 방문하지 않았다면 
                            if region[nr][nc] > rain and not visited[nr][nc]:
                                # 방문처리 
                                visited[nr][nc] = True 
                                queue.append((nr, nc))
                
    if count > max_result:
        max_result = count 

    rain += 1

print(max_result)