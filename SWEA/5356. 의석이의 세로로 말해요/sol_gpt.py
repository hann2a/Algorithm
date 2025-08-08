import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [input() for _ in range(5)]

    # 5개 중 가장 긴 문자열의 길이 구하기 
    max_str = 0
    for i in range(5):
        if len(arr[i]) > max_str:
            max_str = len(arr[i])

    # 문자열 패딩 ('.'으로)
    padded_arr = []
    for row in arr:
        if len(row) < max_str:
            row += '.' * (max_str - len(row))
        padded_arr.append(row)

    # 세로로 읽기
    result = []
    for c in range(max_str):
        for r in range(5):
            char = padded_arr[r][c]
            if char != '.':
                result.append(char)

    # 출력
    print(f"#{test_case} {''.join(result)}")
