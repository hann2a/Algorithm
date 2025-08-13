import sys

sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    num = int(input())
    stat_before = list(map(int, input().split()))
    stat_after = list(map(int, input().split()))

    control = 0 

    change_light = stat_before[:]  # 복사본 만들기

    while change_light != stat_after:
        count = -1  # while 안에서 초기화
        for light in change_light:
            count += 1 
            if light != stat_after[count]:
                control += 1
                # i번째부터 끝까지 토글
                for j in range(count, num):
                    change_light[j] = 1 - change_light[j]
                break  # 하나 바꾸고 다시 처음부터
    
    print(f'#{t} {control}')