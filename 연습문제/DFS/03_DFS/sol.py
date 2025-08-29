import sys
sys.stdin = open('input.txt', 'r')

# 현재 노드위치, 인접행렬, 방문기록, 전체 기록 
def dfs(current_node, adj_matrix, visited, path):
    # 1. 현재 노드 방문 처리 
    visited[current_node] = True 
    path.append(current_node)

    # 2. 현재 노드와 연결된 다른 노드들을 순회
    for next_node in range(1, len(adj_matrix)):
        if adj_matrix[current_node][next_node] and not visited[next_node]:
            dfs(next_node, adj_matrix, visited, path)

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬 생성 (V+1 크기)
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

# 양방향 간선 추가 (간선 정보를 인접행렬에 저장)
for i in range(E):
    n1, n2 = data[i*2], data[i*2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# dfs
visited = [False] * (V+1) # 방문기록 리스트 
whole_path = [] # 전체 탐색 경로를 저장할 리스트 

# 1번 노드부터 시작 
dfs(1, adj_matrix, visited, whole_path)

print(''.join(map(str, whole_path)))