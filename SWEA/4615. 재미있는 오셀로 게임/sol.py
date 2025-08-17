import sys
sys.stdin = open('input.txt', 'r')

# 종료 후 흑돌, 백돌의 개수 
T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]

    # 판 짜기 
    board = [[0] * N for _ in range(N)]
    
    # 초기 보드 설정 추가
    mid = N // 2
    board[mid-1][mid-1] = 2  # 백돌
    board[mid-1][mid] = 1    # 흑돌
    board[mid][mid-1] = 1    # 흑돌
    board[mid][mid] = 2      # 백돌

    # 델타 상하좌우 좌상 우상 좌하 우하 
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 돌 놓고 돌을 바꾸는 로직 
    # 인덱싱 + 1 상태이므로 -1 
    for n in info: # 정보 한 줄 선택 
        # 돌 놓기 (흑돌이든 백돌이든 공통)
        board[n[1]-1][n[0]-1] = n[2]
        
        # 8방향으로 돌 뒤집기
        for i in range(8):
            flipped = []  # 뒤집을 돌들 저장
            nr = n[1] - 1 + dr[i]
            nc = n[0] - 1 + dc[i]
            
            # 해당 방향으로 계속 탐색
            while 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 0:
                if board[nr][nc] == n[2]:  # 같은 색 돌을 만나면
                    # 지금까지 모은 돌들을 뒤집기
                    for fr, fc in flipped:
                        board[fr][fc] = n[2]
                    break
                else:  # 다른 색 돌이면
                    flipped.append((nr, nc))
                
                nr += dr[i]
                nc += dc[i]
    
    # 순회하면서 개수 세기 
    count_black = 0
    count_white = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                count_black += 1
            elif board[r][c] == 2:
                count_white += 1
    
    print(f'#{t} {count_black} {count_white}')