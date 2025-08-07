import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    # test_num : 테스트 번호 
    # array : 배열 
    # 배열의 크기: 100 X 100

    max_sum = 0 

    for i in range(100):
        row_sum = sum(array[i])                
        col_sum = sum(array[r][i] for r in range(100))  
        max_sum = max(max_sum, row_sum, col_sum)


    right_sum = sum(array[k][k] for k in range(100))      
    left_sum  = sum(array[k][99 - k] for k in range(100)) 
    max_sum = max(max_sum, right_sum, left_sum)

    print(f"#{test_case} {max_sum}")
