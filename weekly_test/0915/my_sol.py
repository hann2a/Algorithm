import sys

sys.stdin = open('input.txt', 'r')

def cal_dis(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs(cnt, curr, sum_far):
    global answer

    if sum_far > answer:
        return

    if cnt == N:
        answer = min(answer, sum_far + cal_dis(curr, (0, 0)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, apples[i], sum_far + cal_dis(curr, apples[i]))
            visited[i] = False




T = int(input())
for t in range(1, 1+T):
    N = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    answer = float('inf')

    dfs(0, (0, 0), 0)

    print(f'#{t} {answer}')