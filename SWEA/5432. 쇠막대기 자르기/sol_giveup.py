"""
아래의 쇠막대기는 위의 쇠막대기를 포함 
끝점은 겹치면 안됨
막대기 하나당 레이저는 하나 있어야됨 
레이저는 어떤 끝점과도 겹치지 않음 
레이저 : ()
출력: 잘려진 쇠막대기의 총 개수 
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())

    # 괄호를 숫자 정보로 바꾸기 
    # start_arr: 괄호 개수만큼 0으로 채워진 리스트 
    start_arr = [0] * len(arr)

    # 레이저가 있는 자리에 2를 집어 넣음 
    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] == ')':
            start_arr[i], start_arr[i+1] = 2, 2
        # 나머지는 1 배정 
        elif arr[i] == '(' and arr[i+1] == '(':
            start_arr[i], start_arr[i+1] = 1, 1
        elif arr[i] == ')' and arr[i+1] == ')':
            start_arr[i], start_arr[i+1] = 3, 3
    
    print(start_arr)
    # <-- 여기까지 괄호를 숫자로 바꾼 배열 완성 

    # 레이저 2는 표시 하나만 있어도 됨 
    



    
        
    
