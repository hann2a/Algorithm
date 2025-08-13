"""
N명 예약제
M초의 시간 K개 
손님 도착 시간 -> 기다림 없이 붕어빵을 제공할 수 있는가
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    # N: 몇 명 올거다 
    # M초동안 K개 만들어짐 
    N, M, K = map(int, input().split())
    # second : 각 손님 도착 시간 
    second = list(map(int, input().split()))

    second.sort()

    # M초의 K개를 만드는 배열, 길이는 M 
    stand = [0] * M + [K]

    # 손님이 오는 초를 초과하게 만드는 시간 배열 
    time_line = []
    while len(time_line) <= max(second):
        time_line += stand 
    # <-- 여기서 몇 초마다 붕어빵이 완성된 이어지는 배열 완성 

    # 손님이 도착했을 때 붕어빵이 있는지 확인 
    # second[i] : i번째 도착한 손님이 몇 초에 왔는지 (인덱스)
    # count_carp: 만들어서 쌓이는 붕어빵 개수 
    count_carp = 0 

    # 결과 플래그 추가 
    is_possible = True 

    # 손님의 명 수만큼 반복 
    for i in range(N):
        if i == 0: # 첫 손님
            # 인덱스 second[i]까지 만들어진 붕어빵의 개수가 1개 이상이면 통과 
            if sum(time_line[:second[i]+1]) >= 1:
                count_carp = sum(time_line[:second[i]+1]) -1
            
            # 아니면 Impossible 출력 
            else:
                is_possible = False
                break 
        else: # 두 번째 손님부터  
            # 인덱스 second[i-1] (전에 온 손님의 초 수)+1 부터 second[i](지금 손님의 초수) + count_carp >= 1이면 통과
            if count_carp + sum(time_line[second[i-1]+1:second[i]+1]) >= 1:
                count_carp = count_carp + sum(time_line[second[i-1]+1:second[i]+1]) -1
            else:
                is_possible = False
                break
    if is_possible:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')