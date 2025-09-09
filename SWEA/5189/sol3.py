import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    battery_info = [list(map(int, input().split())) for _ in range(N)]

    # 미리 계산
    battery_list = [i for i in range(1, N)]
    min_battery = float('inf')

    for path in permutations(battery_list, N-1):

        # 첫 번째 칸 가기
        now_battery = 0
        now_battery += battery_info[0][path[0]]

        # 그 이후
        for i in range(N-2):
            now_battery += battery_info[path[i]][path[i+1]]

            # 가지치기
            if now_battery >= min_battery:
                break

        else:
            now_battery += battery_info[path[-1]][0]

            if now_battery < min_battery:
                min_battery = now_battery

    print(f'#{t} {min_battery}')


