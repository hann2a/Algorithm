import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    # 길이 여기서 str로 받음 
    num, length = input().split()

    # 숫자 하나씩 담긴 리스트 
    string = input().split()

    # 여기서 int 버전으로 재할당 
    # 근데 얘 필요한가? < 반복문에서 사용되네 메모리 땜에 준듯 .. 
    length = int(length)

    strto_num = {
        'ZRO': 0, 
        'ONE': 1, 
        'TWO': 2, 
        'THR': 3, 
        'FOR': 4, 
        'FIV': 5, 
        'SIX': 6, 
        'SVN': 7, 
        'EGT': 8, 
        'NIN': 9, 
    }
    
    numto_str = {}

    for k, v in strto_num.items():
        numto_str[v] = k
    # <-- 이 시점에 strto_num의 키와 값이 반전된 버전인 numto_str 완성 


    # string의 숫자 버전 ! 
    converted = []
    
    # 문자에서 숫자로 바꾸기 
    for str_num in string:
        converted.append(strto_num[str_num])
    # <-- 이 시점에 숫자로 된 리스트 완성

    # 숫자 상태에서 정렬 
    for i in range(length-1, 0, -1):
        for j in range(i):
            if converted[j] > converted[j+1]:
                converted[j], converted[j+1] = converted[j+1], converted[j]
    
    # 다시 int로 구성된 converted를 string화 
    result = []
    for num_str in converted:
        result.append(numto_str[num_str])
    # <-- 이 시점에 정렬되었고, str로 구성된 리스트 result 완성 

    print(f"#{test_case}\n", *result)




