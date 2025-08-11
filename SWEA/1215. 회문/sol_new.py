import sys

sys.stdin = open("input.txt", "r")

"""
회문 형태 : A or ABA or ABBA
"""

T = 10

for test_case in range(1, T+1):
    length = int(input())
    arr = [input().strip() for _ in range(8)]

    # 총 회문의 개수 찾기 
    find_palin = 0
    # 가로 회문 찾기 
    for r in range(8):
        for start_c in range(8-length+1):
            # string : 회문 길이만큼 저장하는 변수 
            string = ''
            for c in range(length):
                string += arr[r][start_c + c]
            
            # 문자열 완성 후 검사 
            check = True 
            for i in range(int(length/2)):
                if string[i] != string[length-i-1]:
                    check = False
                    break 
            if check:
                find_palin += 1
    
    # 세로 회문 찾기 
    for c in range(8):
        for start_r in range(8-length+1):
            # string : 회문 길이만큼 저장하는 변수 
            string = ''
            for k in range(length):
                string += arr[start_r + k][c]
            
            # 문자열 완성 후 검사 
            check = True 
            for i in range(int(length/2)):
                if string[i] != string[length-i-1]:
                    check = False
                    break 
            if check:
                find_palin += 1


    print(f"#{test_case} {find_palin}")
