import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    a_i = list(map(int, input().split()))
    b_j = list(map(int, input().split()))

    # N이 클 수도 있고, M이 클 수도 있음 
    max_result = 0 
    if N >= M:
        for i in range(N-M+1): # 첫 번째 걸어놓는 칸 
            sum_multiply = 0 
            for k in range(M):
                sum_multiply += a_i[i+k] * b_j[k]
            if sum_multiply > max_result:
                max_result = sum_multiply 

    elif M > N:
        for i in range(M-N+1): # 첫 번째 걸어놓는 칸 
            sum_multiply = 0 
            for k in range(N):
                sum_multiply += b_j[i+k] * a_i[k]
            if sum_multiply > max_result:
                max_result = sum_multiply
    print(f'#{t} {max_result}')