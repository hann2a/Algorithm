import sys
import itertools

sys.stdin = open('input.txt', 'r')

def calculate_honey(i, j):
    now_honey = honey_bucket[i][j:j+M]
    now_max = 0 

    for count in range(M, 0, -1):
        for subset in itertools.combinations(now_honey, count):
            if sum(subset) > C:
                continue

            profit = 0 
            for honey in subset:
                profit += honey ** 2

            if profit > now_max:
                now_max = profit 
    return now_max

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_bucket = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0 

    for i in range(N):
        for j in range(N-M+1):
            f_honey = calculate_honey(i, j)

            for k in range(i, N):
                if k == i:
                    for v in range(j+M, N-M+1):
                        s_honey = calculate_honey(k, v)
                        max_profit = max(max_profit, f_honey+s_honey)
                else: 
                    for v in range(N-M+1):
                        s_honey = calculate_honey(k, v)
                        max_profit = max(max_profit, f_honey+s_honey)

    print(f'#{t} {max_profit}')