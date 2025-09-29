import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A_i = list(map(int, input().split()))
    B_i = list(map(int, input().split()))

    if N < M:
        long_arr, short_arr = B_i, A_i
    
    else: 
        long_arr, short_arr = A_i, B_i

    max_total = -float('inf')

    for i in range(len(long_arr) - len(short_arr) + 1):
        now_total = 0 

        for j in range(len(short_arr)):

            now_total += short_arr[j] * long_arr[i+j]
        
        if max_total < now_total:
            max_total = now_total 
    
    print(f'#{t} {max_total}')