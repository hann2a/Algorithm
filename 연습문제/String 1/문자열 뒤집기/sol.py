import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    string = input()

    string = string[::-1]

    print(f"{test_case} {string}")