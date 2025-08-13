"""
N을 입력받아 크기 N인 파스칼의 삼각형을 
출력하는 프로그램을 작성하시오 
"""
import sys
sys.stdin = open('input.txt', 'r')
def make_triangle(n):
    tri_list = []
    count = n

    while count != 0:
        if len(tri_list) == 0:
            tri_list.append([1])
            count -= 1
        elif len(tri_list) == 1:
            tri_list.append([1, 1])
            count -= 1
        else: 
            now_line = len(tri_list) # 지금 몇 째줄인지 알려주는 인덱스
            tempo_list = [1] 
            while len(tempo_list) < now_line + 1:
                    now_index = len(tempo_list)
                    if now_index < len(tri_list[now_line-1]):
                        tempo_list.append(tri_list[now_line-1][now_index-1] + tri_list[now_line-1][now_index])
                    else:
                        break
            tempo_list.append(1)
            tri_list.append(tempo_list)
            count -= 1
    return tri_list
        
T = int(input())
for test_case in range(1, T+1):
    line = int(input())
    result = make_triangle(line)
    print(f"#{test_case}")  # 테스트 케이스 번호만 먼저 출력
    for row in result:  # 각 행을 개별적으로 처리
       print(' '.join(map(str, row)))  # 행 내 숫자들만 공백으로 연결하여 출력