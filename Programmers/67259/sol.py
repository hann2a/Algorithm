import heapq

def solution(board):
    n = len(board)
    INF = 10**9

    # 상, 하, 좌, 우 
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 3차원 비용 배열 [r][c][delta]
    cost = [[[INF]*4 for _ in range(n)] for _ in range(n)]

    # 우선순위 큐(최소 힙) 컨테이너 
    pq = []

    for d in range(4):
        cost[0][0][d] = 0 
        heapq.heappush(pq, (0, 0, 0, d)) # (비용, r, c, 방향)
    
    while pq:
        # 최소 비용 pop
        here_cost, r, c, d = heapq.heappop(pq)

        # 같은 상태에 대해 더 싼 비용으로 방문 기록이 있으면 가지치기 
        if here_cost > cost[r][c][d]:
            continue

        # 다익스트라 특성상 처음 도착했을 때의 비용이 곧 최솟값이므로 즉시 반환 
        if (r, c) == (n-1, n-1):
            return here_cost
        
        # 4방향으로 인접 칸 시도. next_d는 다음 방향 인덱스 
        for next_d, (dr, dc) in enumerate(delta):
            nr, nc = r + dr, c + dc

            # 보드 밖이면 pass
            if not (0 <= nr < n and 0 <= nc < n):
                continue 

            # 벽이면 pass
            if board[nr][nc] == 1:
                continue 

            # 같은 방향 유지면 100, 방향 바뀌면 600
            # 새로운 누적 비용 nc 계산 
            add = 100 if d == next_d else 600
            new_cost = here_cost + add

            # 지금 비용이 더 싸면 push 
            if cost[nr][nc][next_d] > new_cost:
                cost[nr][nc][next_d] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, next_d))
    return min(cost[n-1][n-1])
