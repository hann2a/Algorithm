import sys
sys.stdin = open('input.txt', 'r')

def find_top(arr):
    highest = 0 
    for i in range(N):
        for j in range(N):
            if arr[i][j] > highest:
                highest = arr[i][j]
    return highest

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    tracking_map = [list(map(int, input().split())) for _ in range(N)]
    top_point = find_top(tracking_map)

    result = 0 
    visited = [[0] * N for _ in range(N)]