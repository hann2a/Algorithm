import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
"""
컨테이너 수 N 트럭 M 
트럭 당 한 개의 컨테이너 
컨테이너에 실린 화물의 무게, 트럭마다의 적재 용량 
편도로 한 번 운행 
최대 M개의 트럭 운행 
이동한 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력 
"""

for t in range(1, T+1):
    N, M = map(int, input().split())
    loads = list(map(int, input().split()))
    trucks = list(map(int, input().split()))


    # 큰 거부터 차례로 적재하도록
    loads.sort(reverse=True)
    trucks.sort(reverse=True)

    i = j = 0
    total = 0

    while i < N and j < M:
        if loads[i] <= trucks[j]:
            total += loads[i]
            i+= 1
            j += 1
        else:
            i += 1

    print(f'#{t} {total}')
