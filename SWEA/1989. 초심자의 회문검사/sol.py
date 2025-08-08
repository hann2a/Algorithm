import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    string = input()

    if string == string[::-1]:
        result = 1
    else:
        result = 0

    print(f"#{test_case} {result}")