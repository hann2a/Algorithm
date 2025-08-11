import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str2)
    M = len(str1)

    # check : 일치하는 문자열을 확인했는지 여부 
    check = 0

    for i in range(N-M+1):
        count = 0
        for j in range(M):
            if str2[i+j] == str1[j]:
                count += 1
            else: 
                break 

        if count == M:
            check = 1
        
    print(f"#{test_case} {check}")