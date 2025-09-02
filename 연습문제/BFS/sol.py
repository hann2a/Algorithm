import sys
from collections import deque 

sys.stdin = open('input.txt', 'r')

def dfs(start_node, V, adj_list):

    visited = [False] * (V+1)
    all_path = []
    q = deque()

    visited[start_node] = True
    q.append(start_node)

    while q:
        curr_node = q.popleft()
        all_path.append(curr_node)

        for next_node in sorted(adj_list[curr_node]):
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
    return all_path 

V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

result_path = dfs(1, V, adj_list)
print(''.join(map(str, result_path)))