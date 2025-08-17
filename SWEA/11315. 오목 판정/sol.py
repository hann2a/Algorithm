import sys 
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    # arr = [list(input().split()) for _ in range(N)]
    # arr_T = list(map(''.join, zip(*arr)))
    arr = [list(input().strip()) for _ in range(N)]  
    arr_T = [''.join(col) for col in zip(*arr)]     

    result = False
    # 가로 확인 
    for r in range(N):
        count = 0 
        for item in arr[r]:
            if item == 'o':
                count += 1
            elif item == '.':
                if count >= 5:
                    result = True
                else:
                    count = 0
        if count >= 5:
            result = True
    
    # 세로 확인 
    for r in range(N):
        count = 0 
        for item in arr_T[r]:
            if item == 'o':
                count += 1
            elif item == '.':
                if count >= 5:
                    result = True
                else:
                    count = 0
        if count >= 5:
            result = True
    
    # --- 대각선(↘) 전부 확인: 상단행/좌측열에서 시작 ---
    # 상단행에서 시작
    for sc in range(N):                 # (0, sc)
        count = 0
        r, c = 0, sc
        while r < N and c < N:
            if arr[r][c] == 'o':
                count += 1
            else:
                if count >= 5: result = True
                count = 0
            r += 1; c += 1
        if count >= 5: result = True

    # 좌측열에서 시작(주대각선 중복 방지: r=1부터)
    for sr in range(1, N):              # (sr, 0)
        count = 0
        r, c = sr, 0
        while r < N and c < N:
            if arr[r][c] == 'o':
                count += 1
            else:
                if count >= 5: result = True
                count = 0
            r += 1; c += 1
        if count >= 5: result = True

    # --- 대각선(↗) 전부 확인: 하단행/좌측열에서 시작 ---
    # 하단행에서 시작
    for sc in range(N):                 # (N-1, sc)
        count = 0
        r, c = N-1, sc
        while r >= 0 and c < N:
            if arr[r][c] == 'o':
                count += 1
            else:
                if count >= 5: result = True
                count = 0
            r -= 1; c += 1
        if count >= 5: result = True

    # 좌측열에서 시작(중복 방지: r=N-2부터 위로)
    for sr in range(N-2, -1, -1):       # (sr, 0)
        count = 0
        r, c = sr, 0
        while r >= 0 and c < N:
            if arr[r][c] == 'o':
                count += 1
            else:
                if count >= 5: result = True
                count = 0
            r -= 1; c += 1
        if count >= 5: result = True


    if result == True:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{t} {answer}')