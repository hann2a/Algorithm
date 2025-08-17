import sys
sys.stdin = open('input.txt', 'r')

T = 10 
for t in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_T = [list(col) for col in zip(*arr)]
    max_result = 0 

    # 행의 합 
    for r in range(100):
        sum_num = sum(arr[r])
        if sum_num > max_result:
            max_result = sum_num 
    
    # 열의 합 
    for r in range(100):
        sum_num = sum(arr_T[r])
        if sum_num > max_result:
            max_result = sum_num 
    
    # 왼쪽 시작 대각선의 합 
    diag_sum = 0 
    for i in range(100):
        diag_sum += arr[i][i]
    if diag_sum > max_result:
        max_result = diag_sum 
    
    diag_sum2 = 0 
    for i in range(100):
        diag_sum += arr[i][i]
    if diag_sum2 > max_result:
        max_result = diag_sum2

    print(f'#{t} {max_result}')