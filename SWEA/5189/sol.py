import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    battery_table = [list(map(int, input().split())) for _ in range(N)]

    # 방문할 관리 구역 목록 (사무실 0 제외)
    areas_to_visit = [i for i in range(1, N)]
    min_battery = float('inf')

    # 1부터 N-1까지 관리 구역의 모든 방문 순서(순열) 생성
    for path in permutations(areas_to_visit, N-1):
        # 각 경로의 배터리 사용량 계산
        current_battery = 0

        # 1. 사무실(0) 첫 번째 구역
        current_battery += battery_table[0][path[0]]

        # 2. 각 구역 순차 방문
        for i in range(N-2):
            current_battery += battery_table[path[i]][path[i+1]]

            # 가지치기
            if current_battery >= min_battery:
                break
        # 가지치기로 중단된 경우가 아니라면 끝까지 계산
        else:
            # 3. 마지막 구역 -> 사무실(0)
            current_battery += battery_table[path[-1]][0]

            # 최소값 갱신
            min_battery = min(min_battery, current_battery)

    print(f'#{t} {min_battery}')
