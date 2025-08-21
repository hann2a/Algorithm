import sys
sys.stdin = open('input.txt', 'r')

def mini(r, sum_p):
    global ans # answer은 현재 최소합 

    if ans <= sum_p:
        return 
    elif r == N:
        ans = min(ans, sum_p)
        return 
    for j in range(N):
        if v[j]==0:
            v[j] =1
            mini(r+1, sum_p+arr[r][j])
            v[j] = 0




T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N*10
    v = [0] * N
    mini(0, 0)

    print(f'#{t} {ans}')