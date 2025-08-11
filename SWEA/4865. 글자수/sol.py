import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, 1+T):
    str1 = input()
    str2 = input()

    str_dict = {}

    # str1에 있는 글자들을 str_dict()에 정리 
    for c in str1:
        str_dict[c] = 0

    # str2의 글자들을 하나씩 돌면서 만들어놓은 str_dict()에 개수 추가 
    for string in str2:
        for k in str_dict.keys():
            if string == k:
                str_dict[k] = str_dict.get(k) + 1
    
    # max값 초기화 후 비교하면서 최대값 연산 
    max_v = 0
    for v in str_dict.values():
        if v > max_v:
            max_v = v

    print(f"#{test_case} {max_v}")