import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# [0]은 오른쪽으로 가기 [1]은 아래 쪽으로 가기 
dr = [0, 1]
dc = [1, 0]

def dfs(r, c, curr_sum):

    # 종료 조건 
    if r == N-1 and c == N-1:
        return min(min_sum, curr_sum)
    
    for i in range(2):
        nr, nc = r + dr[i], c + dc[i]
        if ( 0<= nr < N and 0 <= nc < N):
            min_sum = dfs(nr, nc, curr_sum+arr[nr][nc], min_sum)

    return min_sum

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sr, sc = 0, 0 
    curr_sum = arr[0][0]
    min_sum = float('inf')
    answer = dfs(sr, sc, curr_sum, min_sum)

    print(f'#{t} {answer}')