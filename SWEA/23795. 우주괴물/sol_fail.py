import sys
sys.stdin = open('input.txt')

T = int(input())

# delta 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 괴물 찾기 
    count_r = 0
    for r in arr:
        count_r += 1
        count_c = 0
        for num in r:
            count_c += 1
            if num == 2:
                # mon_r, mon_c : 괴물의 위치 행, 열 
                mon_r = count_r 
                mon_c = count_c
    
    # 왼쪽 오른쪽 벽 찾기 
    for c in arr[mon_r]:
        nc_l = c + dc[2]
        if nc_l == 1:
            left_c = nc_l
        else:
            pass
        nc_r = c + dc[3]
        if nc_r == 1:
            right_c = nc_r
    
    arr_T = list(map(''.join, zip(*arr)))
    # 위 아래 벽 찾기 
    for c in arr_T[mon_c]:
        nc_u = c + dc[2]
        if nc_u == 1:
            up_c = nc_u
        else:
            pass
        nc_d = c + dc[3]
        if nc_d == 1:
            down_c = nc_d
    
    # 벽 세기 
    count_wall = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                count_wall +=1 
    
    # 광선 세기 
    row = right_c - left_c -2
    column = up_c - down_c -2
    line = row + column 

    # 결과
    result = N*N - line - count_wall 

    print(f"#{t} {result}")