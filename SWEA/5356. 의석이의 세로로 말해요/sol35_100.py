import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    arr = [input() for _ in range(5)]

    max_str = 0
    # 5개 중 가장 긴 문자열의 길이 구하기 
    for i in range(5):
        if len(arr[i]) > max_str:
            max_str = len(arr[i])
    
    # 가장 긴 문자열의 길이에 맞춰서 '.' 추가하기 
    # new_arr: .이 추가돼서 길이가 맞춰진 새로운 리스트 
    new_arr = []
    for i in arr:
        if len(i) < max_str:
            new_arr.append(i + '.' * (max_str - len(i)))
        else:
            new_arr.append(i)

    # 세로로 읽기 
    # prev : 점 빼기 전 요소들이 담긴 result 전 리스트 
    prev = []
    for c in range(0, max_str):
        # pre_str: 한 줄을 다 읽을 때까지만 존재하는 변수 
        pre_str = ''
        for r in range(5):
            pre_str += new_arr[r][c]

        prev.append(pre_str)
    
    # for 문으로 문장 속 점 빼기 
    # result: 점 뺀 조합들의 글자들을 모으는 최종 리스트 
    result = []
    for dot_str in prev:
        # str: 세로로 읽은 줄의 한 글자씩 
        for str in dot_str: 
            if str != '.':
                result.append(str)
            else:
                pass
    # <-- 여기까지 하면 result에 점 뺀 글자들이 순서대로 나열됨 
    print(f"#{test_case} ", *result, sep='')