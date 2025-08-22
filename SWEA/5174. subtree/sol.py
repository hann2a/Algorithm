import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())

    # 노드의 개수 
    V = E + 1 

    # 노드 번호와 인덱스를 일치시키기 위해 V+1 크기로 생성
    # 노드 번호가 1번부터 시작하니까, 인덱스를 편하게 쓰기 위해 V+1 크기로 만드는 것
    left = [0] * (V + 1)  # 각 노드의 왼쪽 자식 정보
    right = [0] * (V + 1)  # 각 노드의 오른쪽 자식 정보

    node_info = list(map(int, input().split()))


    # 간선 정보를 2개씩 (부모, 자식) 짝지어 순회
    for i in range(E):
        parent, child = node_info[i * 2], node_info[i * 2 + 1]

        # parent 노드의 왼쪽 자식이 비어있으면(0) 왼쪽 자식으로 등록
        if left[parent] == 0:
            left[parent] = child
        # 왼쪽 자식이 이미 있다면, 오른쪽 자식으로 등록
        else:
            right[parent] = child
        def size(node):
            if node == 0:
                return 0
            return 1 + size(left[node]) + size(right[node])
    count = size(N)

    print(f'#{t} {count}')