import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(1, T+1):
    N = int(input()) # 건물의 개수 
    arr = list(map(int, input().split()))

    # count : 세대 수 세기 
    count = 0 
    for i in range(2, N-1):
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            count += arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
    
    print(f'#{t} {count}')