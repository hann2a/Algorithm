from collections import deque

def solution(n, path, order):
    # 1) 트리에서 0을 루트로 부모-자식 방향 만들기
    adj = [[] for _ in range(n)]
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    parent = [-1]*n
    tree = [[] for _ in range(n)]  # parent -> child
    q = deque([0])
    parent[0] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                tree[u].append(v)
                q.append(v)

    # 2) DAG 구성: (부모->자식) + (order: a->b)
    dag = [[] for _ in range(n)]
    indeg = [0]*n

    # 부모->자식 간선
    for u in range(n):
        for v in tree[u]:
            dag[u].append(v)
            indeg[v] += 1

    # order 간선
    for a, b in order:
        # 시작 노드 0이 '나중'이면 시작 불가
        if b == 0:
            return False
        dag[a].append(b)
        indeg[b] += 1

    # 시작 자체가 막혀 있으면 불가
    if indeg[0] > 0:
        return False

    # 3) 위상 정렬(Kahn)
    dq = deque([i for i in range(n) if indeg[i] == 0])
    seen = 0
    while dq:
        u = dq.popleft()
        seen += 1
        for v in dag[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)

    return seen == n
