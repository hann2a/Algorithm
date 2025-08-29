import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기 
edge_data =  list(map(int, input().split()))

# 1. V + 1 * V + 1 크기의 2차원 리스트를 0으로 초기화 
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
print(adj_matrix)

# --- 결과 확인 ---
