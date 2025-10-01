import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j, visited):
    pass

visited = []
for i in range(N):
    for j in range(N):
        dfs(0, 0, visited)
