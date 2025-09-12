import sys

sys.stdin = open('input.txt', 'r')

def dfs():
    pass

T = int(input())
for t in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(4)]

    for i in range(4):
        for j in range(4):
            dfs(i, j)