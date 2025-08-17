import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = [list(col) for col in zip(*arr)]
    
    result_count = 0 

    # 가로로 세기 
    for i in range(N): # 1 2 3 4 5 ...
        # count: 하얀 칸 세어주는 변수 
        # collection: 임시로 카운트 수집하는 리스트 
        count = 0 
        collection = []
        for item in arr[i]:
            if item == 1:
                count += 1
            elif item == 0:
                if count != 0:
                    collection.append(count)
                    count = 0
        if count:
            collection.append(count)
        for k in collection:
            if k == K:
                result_count += 1
    
    # 세로로 세기 
    for i in range(N): # 1 2 3 4 5 ...
        # count: 하얀 칸 세어주는 변수 
        # collection: 임시로 카운트 수집하는 리스트 
        count = 0 
        collection = []
        for item in arr_T[i]:
            if item == 1:
                count += 1
            elif item == 0:
                if count != 0:
                    collection.append(count)
                    count = 0
        if count:
            collection.append(count)
        for k in collection:
            if k == K:
                result_count += 1

    print(f'#{t} {result_count}')