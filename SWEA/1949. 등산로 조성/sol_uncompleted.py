import sys

sys.stdin = open('input.txt', 'r')

"""
N * N 등산로 
값은 지형의 높이 

<조건>
1. 가장 높은 봉우리 
2. 대각선 연결 x, 높이가 같은 곳끼리 연결 x, 높은 곳에서 낮은 곳으로 
3. 딱 한 곳만 최대 k 만큼 지형을 깎는 공사 가능 
가장 긴 등산로를 찾아 '그 길이'를 출력 
K는 1이상 5이하 
지형의 높이는 1 이상 20 이하 
가장 높은 봉우리는 최대 5개 
높이를 1보다 작게 만드는 것도 가능하다 
"""

# delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_longest_path(arr, start_r, start_c):
    # 큐 대신 리스트로 현재 탐색 중인 경로들 관리
    paths = [(start_r, start_c, 1)]  # (r, c, 길이)
    max_len = 1
    
    while paths:
        new_paths = []
        for r, c, length in paths:
            # 4방향 탐색
            for nr, nc in 인접칸들:
                if 갈수있으면:
                    new_paths.append((nr, nc, length+1))
                    max_len = max(max_len, length+1)
        paths = new_paths
    
    return max_len
                     











T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


