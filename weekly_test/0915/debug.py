import sys
sys.stdin = open('input.txt')
# SSAFY 과평5 - 사과 수학 (DFS 트레이싱 버전)
# N이 크면 로그가 매우 길어지니, 먼저 N=3~4 정도로 테스트 추천

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# ===== 트레이스 유틸 =====
DEBUG = True          # 로그 보기/숨기기
MAX_LOG = 20000       # 로그 줄 수 제한 (너무 길어질 때 안전장치)
log_count = 0

def log(depth, *args):
    global log_count
    if not DEBUG or log_count >= MAX_LOG:
        return
    print("  " * depth + " ".join(str(x) for x in args))
    log_count += 1
# ========================

def dfs(cnt, last_idx, dist_sum, depth):
    """
    cnt     : 방문한 사과 수
    last_idx: 마지막으로 선 위치(노드 index). 0=창고, 1..N=사과
    dist_sum: 지금까지 누적 거리
    depth   : 재귀 깊이(들여쓰기용)
    """
    global ans, visited, N, dist

    # --- 가지치기 직전 로그 ---
    log(depth, f"[ENTER] cnt={cnt}, last={last_idx}, sum={dist_sum}, path={path}")

    # 가지치기
    if dist_sum >= ans:
        log(depth, f"[PRUNE] sum {dist_sum} >= best {ans} -> return")
        log(depth, f"[EXIT ] cnt={cnt}, last={last_idx}")  # 함수가 닫힘
        return

    # 모든 사과 방문 완료 → 창고 복귀
    if cnt == N:
        total = dist_sum + dist[last_idx][0]
        log(depth, f"[COMPLETE] back_to_0 +{dist[last_idx][0]} => total={total}")
        if total < ans:
            ans = total
            log(depth, f"[BEST] ans <- {ans}")
        log(depth, f"[EXIT ] cnt={cnt}, last={last_idx}")  # 함수가 닫힘
        return

    # 다음 사과 시도
    for nxt in range(1, N+1):
        if not visited[nxt]:
            visited[nxt] = True
            path.append(nxt)  # 디버그용(방문 순서)
            step = dist[last_idx][nxt]
            log(depth, f"-> TRY nxt={nxt} (+{step})")
            dfs(cnt+1, nxt, dist_sum + step, depth+1)
            # 백트래킹(함수 닫힌 뒤 되돌림)
            path.pop()
            visited[nxt] = False
            log(depth, f"<- BACK from {nxt} (restore state)")

    log(depth, f"[EXIT ] cnt={cnt}, last={last_idx}")  # 이 지점에서 함수가 닫힘


# ===== 입력 및 실행 =====
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(N)]

    # 노드 0=(0,0), 1..N=사과
    pts = [(0,0)] + apples

    # 거리 미리 계산
    dist = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            dist[i][j] = manhattan(pts[i], pts[j])

    visited = [False]*(N+1)
    ans = 10**9
    path = []  # 방문 순서 기록(디버그용)

    # 시작: (0)에서 각 사과로 가는 DFS를 통일적으로 처리하기 위해
    # dfs 안에서 last_idx=0, cnt=0, sum=0으로 시작
    log_count = 0
    dfs(0, 0, 0, 0)

    # 최종 답
    print(f"#{tc} {ans}")
