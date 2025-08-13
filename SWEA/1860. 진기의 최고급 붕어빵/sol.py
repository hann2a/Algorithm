import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    # N: 손님 수, M: 만드는데 걸리는 시간, K: M초마다 만들어지는 개수
    N, M, K = map(int, input().split())
    # 각 손님 도착 시간
    arrivals = list(map(int, input().split()))
    
    # 시간 순서대로 정렬
    arrivals.sort()
    
    possible = True
    
    for i in range(N):
        arrival_time = arrivals[i]
        
        # arrival_time까지 만들어진 총 붕어빵 개수
        total_made = (arrival_time // M) * K
        
        # 지금까지 온 손님 수 (현재 손님 포함)
        customers_so_far = i + 1
        
        # 붕어빵이 부족하면 Impossible
        if total_made < customers_so_far:
            possible = False
            break
    
    if possible:
        print(f"#{t} Possible")
    else:
        print(f"#{t} Impossible")