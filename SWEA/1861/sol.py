import sys
sys.stdin = open('input.txt', 'r')

# 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def go_next(r, c, count):
    longest = count

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
            return go_next(nr, nc, count + 1)

    return longest



T = int(input())
for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    result_num = 0

    for i in range(N):
        for j in range(N):
            now_count = go_next(i, j, 1) # 시작 칸 포함 1부터
            if (now_count > max_count) or (now_count == max_count and arr[i][j] < result_num):
                max_count = now_count
                result_num = arr[i][j]


    print(f'#{t} {result_num} {max_count}')