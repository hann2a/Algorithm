import sys

sys.stdin = open('input.txt')


# # 중위 순회(Inorder Traversal)
def link(node_index):
    """
    node_index: 현재 노드 인덱스
    노드 형식:
      - [idx, ch]                       # 리프
      - [idx, ch, left_idx, right_idx]  # 내부
    """
    L = len(sentence[node_index])
    s = sentence[node_index][1]

    if L == 2:
        # 리프
        result.append(s)
        return

    if L == 3:
        # 자식 1개만 있는 노드
        left_child = int(sentence[node_index][2])
        link(left_child)
        result.append(s)  # 왼 - 자기
        return

    if L == 4:
        # 좌·우 자식 모두 있는 노드
        left_child = int(sentence[node_index][2])
        right_child = int(sentence[node_index][3])
        link(left_child)
        result.append(s)   # 왼 - 자기 - 오 
        link(right_child)
        return


T = 10
for t in range(1, T+1):
    N = int(input().strip())
    sentence = [[] for _ in range(N+1)]
    for _ in range(N):
        parts = input().split()
        sentence[int(parts[0])] = parts

    result = []           
    link(1)                   
    result_sentence = ''.join(result)

    print(f'#{t} {result_sentence}')
