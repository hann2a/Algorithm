import sys
import itertools

sys.stdin = open('input.txt', 'r')

def calc_battery(all_path):
    global min_consume
    now_consume = 0

    for i in range(1, N+1):
        start, end = all_path[i-1], all_path[i]
        now_consume += arr[start][end]

    if now_consume < min_consume:
        min_consume = now_consume
    return

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_consume = float('inf')

    # 한 조합당 계산
    for subset in itertools.permutations(range(2, N+1), N-1):
        all_path = [1]
        for i in subset:
            all_path.append(i)

        all_path.append(1)

        # <-- 모든 경로 만듦

        calc_battery(all_path)

    print(f'#{t} {min_consume}')
