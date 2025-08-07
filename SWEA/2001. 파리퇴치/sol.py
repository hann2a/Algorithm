import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # max_box: 최대값 저장하는 변수 
    max_box = 0 
    # now_point: 박스 자체가 틀을 벗어나지 않는 선에서 
    # 왼쪽 위부터 순회하는 변수 
    for r in range(0, N-M+1):
        for c in range(0, N-M+1):
            now_point = arr[r][c]
            # box: 박스 하나가 다 만들어질 때까지만 저장되고 초기화되는 변수 
            box = 0 
            for i in range(M): # 행
                for j in range(M): # 열 
                    # now_point에서 M값만큼 순회하는 로직 
                    box += arr[r+i][c+j]
                    max_box = max(max_box, box)
    
    print(f"#{test_case} {max_box}")