# SSAFY 과평5 - 문제2: 사과 수학
# DFS + 백트래킹 + 가지치기
import sys

sys.stdin = open('input.txt', 'r')
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs(cnt, curr, dist_sum):
    global ans
    # 가지치기
    if dist_sum >= ans:
        return

    # 모든 사과 방문 완료
    if cnt == N:
        ans = min(ans, dist_sum + manhattan(curr, (0, 0)))
        return

    # 다음 사과 방문
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, apples[i], dist_sum + manhattan(curr, apples[i]))
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    ans = 10**9

    dfs(0, (0,0), 0)

    print(f"#{tc} {ans}")