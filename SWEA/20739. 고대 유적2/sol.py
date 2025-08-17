import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = [list(col) for col in zip(*arr)]

    max_result = 0 
        # 가로로 세기 
    for i in range(N): # 1 2 3 4 5 ...
        # count: 구조물 세어주는 변수 
        count = 0 
        for item in arr[i]:
            if item == 1:
                count += 1
            elif item == 0:
                if count != 0:
                    if max_result < count and count != 1:
                        max_result = count
                    count = 0
        if count != 1:
            if max_result <count:
                max_result = count 
        
    
    # 세로로 세기 
    for i in range(M): 
        count = 0 
        collection = []
        for item in arr_T[i]:
            if item == 1:
                count += 1
            elif item == 0:
                if count != 0:
                    if max_result < count and count != 1:
                        max_result = count
                    count = 0
        if count != 1:
            if max_result <count:
                max_result = count 

    print(f'#{t} {max_result}')