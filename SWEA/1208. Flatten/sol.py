import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, 1+T):
    dump = int(input())
    arr = list(map(int, input().split()))

    # 오름차순 정렬해서 뒤에서 깎아서 앞에 추가할 거 
    arr.sort()
    # 깎으면서 덤프 횟수 셈 
    count_dump = dump 
    while count_dump != 0:
        # 평탄화 조건을 충족하면 while문 빠져나옴 
        if max(arr) - min(arr) <= 1:
            break
        # 제일 큰 거에서 하나 빼고 제일 작은 거 하나 더해주기 
        arr[-1] -= 1
        arr[0] += 1
        # 수 바뀌었으니까 한 번 더 정렬 
        arr.sort()
        # 모두 수행했으니까 덤프 한 번 차감 
        count_dump -= 1
    result = max(arr) - min(arr)

    print(f'#{t} {result}')