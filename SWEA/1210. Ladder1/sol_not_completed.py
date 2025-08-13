import sys
sys.stdin = open("input.txt", "r")

T = 10 
for test_case in range(1, T+1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 사다리 타기는 아래, 왼쪽, 오른쪽만 사용 
    dr = [1, 0, 0] 
    dc = [0,-1, 1]
    # 행과 열을 뒤집어서 도착점을 출발점처럼 만들기 
    arr = [row[::-1] for row in arr[::-1]]

    # 출발점 찾기 (0, 2인점의 인덱스)
    count = -1 
    for k in arr[0]:
        count += 1
        if k == 2:
            row, column = 0, count 

    # 시작 방향 
    d = 0

    # 일단 아래로 한 칸 내려가고 오른쪽 왼쪽을 봄 
    # 항상 내려간 다음에, 왼오 살피고, 그 다음에 다시 내려감 
    # 0: 아래 1: 왼 2: 오른쪽 

    for r in range(100):
        nr = 
        nc = 

    now_point = arr[0, column]
    if arr[0, colu]
    

        #     nr, nc = r + dr[d], c + dc[d]
        # # 경계 또는 이미 방문 했으면 방향 회전
        #     if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] != 0:
        #         d = (d + 1) % 4 
        #         nr, nc = r + dr[d], c + dc[d]
        #     r, c = nr, nc 
        # return arr 