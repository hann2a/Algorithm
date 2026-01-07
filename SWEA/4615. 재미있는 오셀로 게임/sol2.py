
def solve_othello(N, M, moves):
    # 1. 보드 초기화
    # N*N 크기의 보드를 0으로 채움 (1-based indexing을 편하게 쓰기 위해 N+1 크기 사용도 가능하지만, 
    # 여기선 0-based indexing으로 설명하고 좌표 변환을 보여드리겠습니다)
    board = [[0] * N for _ in range(N)]
    
    # 돌의 색깔 정의 (문제에서 1: 흑돌, 2: 백돌)
    BLACK = 1
    WHITE = 2
    
    # 초기 돌 배치 (문제 조건: 중앙에 배치)
    # 예: N=4일 때 (1,1), (2,2)는 백돌, (1,2), (2,1)는 흑돌
    # 0-based index로 변환하면:
    center = N // 2
    board[center-1][center-1] = WHITE
    board[center][center] = WHITE
    board[center-1][center] = BLACK
    board[center][center-1] = BLACK
    
    # 2. 8방향 델타 이동 정의
    # (위, 아래, 왼쪽, 오른쪽, 대각선 4개)
    # 델타를 쓰는 이유: 8개의 방향을 일일이 if문으로 짜면 코드가 너무 길어지고 복잡해집니다.
    # dr (row 변화량), dc (col 변화량)
    drc = [(-1, 0), (1, 0), (0, -1), (0, 1),  # 상하좌우
           (-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선

    for col, row, color in moves:
        # 입력 좌표가 1부터 시작하므로 0-based index로 맞춰줍니다.
        r, c = row - 1, col - 1
        
        # 돌을 일단 놓습니다.
        board[r][c] = color
        
        # 3. 뒤집기 로직 (핵심!)
        # 놓은 돌(r, c)을 기준으로 8방향을 모두 탐색합니다.
        for dr, dc in drc:
            # 이번 방향에서 뒤집을 수 있는 상대 돌들을 임시로 저장할 리스트
            candidates = []
            
            # 현재 위치에서 해당 방향으로 한 칸씩 계속 이동해봅니다.
            nr, nc = r + dr, c + dc
            
            while True:
                # 3-1. 보드 범위를 벗어나면 중단 (이 방향으로는 뒤집기 불가)
                if not (0 <= nr < N and 0 <= nc < N):
                    break
                
                # 3-2. 빈 칸을 만나면 중단 (돌이 끊겨있으므로 뒤집기 불가)
                if board[nr][nc] == 0:
                    break
                
                # 3-3. 같은 색 돌을 만났다! -> 샌드위치 완성
                if board[nr][nc] == color:
                    # 지금까지 모아둔 상대 돌(candidates)을 모두 뒤집습니다.
                    # Q1. 뒤집는 걸 코드에 어떻게 반영하나요?
                    # A. candidates에 저장된 좌표들의 값을 현재 내 돌의 색(color)으로 덮어씌우면 됩니다.
                    for cr, cc in candidates:
                        board[cr][cc] = color
                    # 이 방향 탐색 종료 (더 갈 필요 없음)
                    break
                
                # 3-4. 상대 돌을 만났다 -> 뒤집을 후보에 추가하고 계속 전진
                # 내 돌(color)도 아니고 빈 칸(0)도 아니면 상대 돌입니다.
                candidates.append((nr, nc))
                
                # 다음 칸으로 이동
                nr += dr
                nc += dc

    # 결과 계산: 흑돌, 백돌 개수 세기
    black_count = 0
    white_count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == BLACK:
                black_count += 1
            elif board[i][j] == WHITE:
                white_count += 1
                
    return black_count, white_count

# 테스트 실행 예시 (문제 예제 입력과 유사하게 구성)
if __name__ == "__main__":
    # N=4, 플레이가 (2,3,흑), (3,4,백) ... 이런 식으로 들어온다고 가정
    test_N = 4
    test_M = 12 # 이동 횟수 (테스트용 임의 값)
    # (col, row, color)
    test_moves = [
        (2, 3, 1), (2, 2, 2), (3, 2, 1) # 예시 데이터
        # ... 실제 문제 데이터를 넣어서 테스트 가능
    ]
    
    # 실제 실행 시 주석 해제
    # b, w = solve_othello(test_N, test_M, test_moves)
    # print(f"흑돌: {b}, 백돌: {w}")
