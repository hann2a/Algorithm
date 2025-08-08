import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    arr = [input() for _ in range(5)]
    
    # 5개 중 가장 긴 문자열의 길이 구하기 
    max_str = 0
    for i in range(5):
        if len(arr[i]) > max_str:
            max_str = len(arr[i])
    
    result = []
    for c in range(max_str):
        for r in range(5):
            if c < len(arr[r]):     
                result.append(arr[r][c])
    print(f"#{test_case} ", *result, sep='')