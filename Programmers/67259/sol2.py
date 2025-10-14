import heapq

def solution(board):
    n = len(board)
    INF = 10**9

    # 방향 배열 
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 3차원 비용 배열 
    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    pq = []

    for d in range(4):
        cost[0][0][d] = 0 
        heapq.heappush(pq, (0, 0, 0, d))

    while pq:
        here_cost, r, c, d = heapq.heappop(pq)

        # 만약 꺼낸 비용이 지금 기록된 비용보다 크다면 미리 가지치기 
        if here_cost > cost[r][c][d]:
            continue 

        # 만약 pop하자마자 확인했는데 r, c가 마지막 칸이라면 지금 비용을 바로 push
        if (r, c) == (n-1, n-1):
            return here_cost 
        
        # 이제 4방향 돌자 
        for next_d, (dr, dc) in enumerate(delta):
            nr, nc = r + dr, c + dc

            # 만약 보드를 벗어난다면 가지치기 
            if not (0 <= nr < n and 0 <= nc < n):
                continue 

            # 만약 새로간 칸이 벽이라면 가지치기
            if board[nr][nc] == 1:
                continue 

            # 이제 비용 갱신해야지 
            add = 100 if d == next_d else 600
            next_cost = here_cost + add

            if next_cost < cost[nr][nc][next_d]:
                cost[nr][nc][next_d] = next_cost
                heapq.heappush(pq, (next_cost, nr, nc, next_d))
    return min(cost[n-1][n-1])




