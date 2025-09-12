# 실행시간 139 ms with gpt
import sys
sys.stdin = open('input.txt', 'r')

# 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def go_next(r, c, count):
    # 이미 (r,c)의 결과가 있으면, 현재까지 누적한 count와 합쳐서 반환
    if dp[r][c]:
        return (count - 1) + dp[r][c]

    best = count  # 현재까지 길이(최소 자기 자신)
    has_next = False

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
            has_next = True
            best = max(best, go_next(nr, nc, count + 1))
            # 1861 조건(숫자 유일)이면 아래처럼 바로 리턴해도 됨:
            # return go_next(nr, nc, count + 1)

    # (r,c)에서의 최대 길이를 dp에 저장
    # best는 "시작점에서의 총 길이"고, (r,c)에서의 길이는 best - (count - 1)
    dp[r][c] = best - (count - 1)
    return best


T = int(input())
for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]  # 메모이제이션 테이블

    max_count = 0
    result_num = 0

    for i in range(N):
        for j in range(N):
            now_count = go_next(i, j, 1)  # 시작 칸 포함 → 1
            # 더 길거나, 같으면 시작 숫자가 작은 쪽
            if (now_count > max_count) or (now_count == max_count and arr[i][j] < result_num):
                max_count = now_count
                result_num = arr[i][j]

    print(f'#{t} {result_num} {max_count}')
