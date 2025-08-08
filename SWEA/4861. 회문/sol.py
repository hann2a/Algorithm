import sys
sys.stdin = open("input.txt", "r")

"""
N x N의 배열 
회문의 길이 M 
"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    
    # 최종 결과 회문 저장 변수 
    result = '' 
    # 가로 세로를 한 번에 할 수 있을듯 <- 못해 ! 
    # 왜 안됐냐 : 가로 기준으로 돌 때(세로 기준으로 돌 때) 세로(가로)는 끝까지 돌아야
    #            되는데 막히게 됨 ... 분리하자 
    
    # 가로 회문 
    for r in range(N):                      # 모든 행
        for c in range(N - M + 1):          # 시작 열: c ~ c+M-1 이 N을 넘지 않게
            row_sent = ''
            for i in range(M):
                row_sent += arr[r][c + i]
            if row_sent == row_sent[::-1]:
                result = row_sent
    # 세로 회문 
    for c in range(N):                      # 모든 열
        for r in range(N - M + 1):          # 시작 행: r ~ r+M-1 이 N을 넘지 않게
            column_sent = ''
            for i in range(M):
                column_sent += arr[r + i][c]
            if column_sent == column_sent[::-1]:
                result = column_sent
    
    print(f"#{test_case} {result}")
