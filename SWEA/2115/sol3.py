import sys, itertools 


sys.stdin = open('input.txt', 'r')

def calculate_honey(i, j):
    now_honey = honey_bucket[i][j:j+M]
    result_honey = 0 

    for count in range(M, 0, -1):
        for subset in itertools.combinations(now_honey, count):
            # 더한게 C를 넘어가면 반복문 끝 
            if sum(subset) > C:
                continue 

            sum_honey = 0

            for honey in subset:
                sum_honey += honey ** 2
            
            if sum_honey > result_honey:
                result_honey = sum_honey 

    return result_honey 
T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_bucket = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0 

    # 첫 번째 꿀통 첫 번째 칸 정하기 
    for i in range(N):
        for j in range(N-M+1):
            f_honey = calculate_honey(i, j)

            # 두 번째 꿀통 첫 번째 칸 정하기 
            for k in range(i, N):

                # 같은 열일 때 
                if k == i:
                    for v in range(j+M,  N-M+1):
                        s_honey = calculate_honey(k, v)
                        max_profit = max(max_profit, f_honey+s_honey)
                # 다른 열일 때 
                else: 
                    for v in range(N-M+1):
                        s_honey = calculate_honey(k, v)
                        max_profit = max(max_profit, f_honey+s_honey)
    
    print(f'#{t} {max_profit}')