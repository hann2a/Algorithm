import sys, itertools

sys.stdin = open('input.txt', 'r')

def honey_square(arr):
    square_value = 0
    for i in arr:
        square_value += i**2
    return square_value

def calculate_honey(i, j):
    now_list = honey_bowl[i][j:j + M]
    best_profit = 0

    for i in range(M, 0, -1):
        for subset in itertools.combinations(now_list, i):
            if sum(subset) > C:
                continue
            profit = 0
            for honey in subset:
                profit += honey ** 2

            if profit > best_profit:
                best_profit = profit
    return best_profit

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_bowl = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0
    # 첫번째 벌꿀 통 첫 번째 칸 선택하기
    for i in range(N):
        for j in range(N-M+1):
            f_honey = calculate_honey(i, j)
            # 두 번째 벌꿀 통 두 번째 칸  선택하기
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




