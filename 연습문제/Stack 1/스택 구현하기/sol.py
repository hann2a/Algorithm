import sys

sys.stdin = open('input.txt', 'r', encoding='utf-8')

stack  = []

T = 3
for tc in range(1, T+1):
    string = input().strip()

    stack.append(string)

while stack:
    print(stack.pop())