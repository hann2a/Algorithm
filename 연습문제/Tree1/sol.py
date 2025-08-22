import sys

sys.stdin = open('input.txt')

def vlr(node):
    if node != 0:
        print(node, end=' ')

        vlr(left[node])
        vlr(right[node])
# ---- 트리 저장을 위한 자료구조 준비 ----
V = int(input())  # V: 정점(Vertex)의 총 수
E = V - 1  # E: 간선(Edge)의 수

left = [0] * (V + 1)  # 각 노드의 왼쪽 자식 정보
right = [0] * (V + 1)  # 각 노드의 오른쪽 자식 정보

edge = list(map(int, input().split()))

# 간선 정보를 2개씩 (부모, 자식) 짝지어 순회
for i in range(E):
    parent, child = edge[i * 2], edge[i * 2 + 1]

    # parent 노드의 왼쪽 자식이 비어있으면(0) 왼쪽 자식으로 등록
    if left[parent] == 0:
        left[parent] = child
    # 왼쪽 자식이 이미 있다면, 오른쪽 자식으로 등록
    else:
        right[parent] = child

root = 1

vlr(root)
