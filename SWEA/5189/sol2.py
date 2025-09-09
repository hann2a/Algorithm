import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, 1+T):
    N = int(input())
    battery_info = [list(map(int, input().split())) for _ in range(N)]

    # 출발 전 정보 만들기
    battery_list = [i for i in range(1, N)]
    min_battery = float('inf')

    # 조합 만들기
    for path in permutations(battery_list, N-1):

        now_battery = 0
        # 첫 번째
        now_battery += battery_info[0][path[0]]

        # 돌면서 추가
        for i in range(N-2):
            now_battery += battery_info[path[i]][path[i+1]]

            if now_battery >= min_battery:
                break

        else:
            now_battery += battery_info[path[-1]][0]

            if min_battery > now_battery:
                min_battery = now_battery

    print(f'#{t} {min_battery}')

