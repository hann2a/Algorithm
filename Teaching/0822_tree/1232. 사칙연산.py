import sys

sys.stdin = open('input2.txt', 'r')

def calc(node_index):
    """
    node_index: 현재 계산할 노드의 번호 

    기저 조건: 재귀의 탈출 조건 -> 리프노드 // 길이가 2 
    """
    if len(tree[node_index]) == 2:
        return int(tree[node_index][1])

    else:
        left_child = int(tree[node_index][2])
        right_child = int(tree[node_index][3])

        left_val = calc(left_child)
        right_val = calc(right_child)

        operate = tree[node_index][1]
        if operate == '+':
            return left_val + right_val
        elif operate == '-':
            return left_val - right_val
        elif operate == '*':
            return left_val * right_val
        else:
            return left_val // right_val
        
T = 10 
for t in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N):
        node_input = input().split()
        # print(node_input)
        # print(node_input[0])
        tree[int(node_input[0])] = node_input
        # print(tree)

    result = calc(1)

    print(f'#{t} {result}')
    