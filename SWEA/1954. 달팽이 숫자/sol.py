import sys
sys.stdin = open("input.txt", "r")

T = int(input())

"""
N x N의 달팽이 배열 
"""
for test_case in range(1, T+1):
    N = int(input())

    dr = [0, 1, 0,-1] 
    dc = [1, 0,-1, 0]
    
    def make_snail(N):
        arr = [[0]*N for _ in range(N)]
        r, c, d = 0, 0, 0 # 시작 위치와 방향
        for num in range(1, N*N + 1):
            arr[r][c] = num    # 현재 칸 기록
        # 다음 칸 시도
            nr, nc = r + dr[d], c + dc[d]
        # 경계 또는 이미 방문 했으면 방향 회전
            if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] != 0:
                d = (d + 1) % 4 
                nr, nc = r + dr[d], c + dc[d]
            r, c = nr, nc 
        return arr 
    
    result = make_snail(N)
    print(f"#{test_case}")
    for row in result:
        print(*row)