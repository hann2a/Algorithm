import sys

sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# (r, c) 좌표, 현재 등산로 길이, 공사(cut) 진행 여부를 인자로 받는 탐색 함수 
def explore_path(r, c, road_len, cut_done):
    global max_len

    # 현재까지 만들어진 등산로 길이가 최대 길이라면 갱신 
    if max_len < road_len:
        max_len = road_len

    # 현재 위치를 방문했다고 표시 
    visited[r][c] = 1

    # 현재 위치 (r, c)에서 델타 탐색으로 상하좌우 네 방향의 이웃을 확인
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 다음 위치가 지도 범위 안이고 아직 방문하지 않았다면 
        if 0 <=nr < N and 0 <= nc <N and not visited[nr][nc]:
            # 조건1. 공사 없이 이동 가능한 경우 (다음 장소가 더 낮은 지형)
            if grid[r][c] > grid[nr][nc]:
                explore_path(nr, nc, road_len + 1, cut_done)
            # 조건2. 공사를 통해 이동한 경우 
            # 아직 공사를 안했고, 다음 장소를 k만큼 깎았을 때 현재보다 낮아진다면 
            elif not cut_done and grid[r][c] > grid[nr][nc] - K:
                original_height = grid[nr][nc]
                grid[nr][nc] = grid[r][c] - 1
                explore_path(nr, nc, road_len + 1, True)
                grid[nr][nc] = original_height
    
    visited[r][c] = 0 
        

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 1. 지도에서 가장 높은 봉우리의 높이를 찾음 
    max_h = 0
    for r in range(N):
        for c in range(N):
            if max_h < grid[r][c]:
                max_h = grid[r][c]
    
    # 2. 가장 긴 등산로의 길이를 저장할 변수 초기화 
    max_len = 0

    # 3. 가장 높은 모든 봉우리에서 탐색 시작 
    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_h:
                explore_path(r, c, 1, False)
    
    print(f'#{t} {max_len}')