import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 카운트 수를 세어주는 함수 
def count_pages(total, target):
    left, right = 1, total
    cnt = 0
    while True:
        mid = (left + right) // 2   # 정확한 가운데
        cnt += 1                 
        if mid == target:
            return cnt
        elif mid > target:          # 범위를 좁혀줌 
            right = mid
        else:                       # mid < target
            left = mid


for test_case in range(1, T+1):
    page, A, B = map(int, input().split())

    a = count_pages(page, A)
    b = count_pages(page, B)

    # 카운트 수 비교해서 결과 출력 
    if a > b:
        result = 'B'
    elif a < b:
        result = 'A'
    else:
        result = 0

    print(f"#{test_case} {result}")