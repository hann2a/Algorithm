import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

dr = [0, 1]
dc = [1, 0]

def dfs(r, c, curr_sum):
    global min_sum

    # 가지치기 
    if curr_sum > min_sum:
        return

    # 종료조건 
    if r == N-1 and c == N-1:
        if curr_sum < min_sum:
            min_sum = curr_sum 
        return 
    
    for i in range(2):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, curr_sum+arr[nr][nc])


for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sr, sc = 0, 0 
    curr_sum = arr[sr][sc]
    min_sum = float('inf')

    dfs(sr, sc, curr_sum)

    print(f'#{t} {min_sum}')