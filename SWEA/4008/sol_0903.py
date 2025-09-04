import sys, itertools

sys.stdin = open('input.txt', 'r')

"""
왼쪽에서 오른쪽으로 순서대로 계산 
그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오 
N: 숫자 개수 
N-1: 연산자 개수 
숫자 1~9
나눗셈 시 소숫점은 버린다 
숫자의 순서는 변경할 수 없다(연산자만 변경 가능)
"""

def calculate(index, number, add, sub, mul, div):
    global min_result
    global max_result

    # 종료조건
    if index == N:
        if number < min_result:
            min_result = number
        if number > max_result:
            max_result = number
        return

    if add:
        calculate(index+1, number+numbers[index], add-1, sub, mul, div)
    if sub:
        calculate(index+1, number-numbers[index], add, sub-1, mul, div)
    if mul:
        calculate(index+1, number*numbers[index], add, sub, mul-1, div)
    if div:
        calculate(index+1, int(number/numbers[index]), add, sub, mul, div-1)



T = int(input())

for t in range(1, T+1):
    N = int(input()) #len(numbers)
    add, sub, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(N, calculator, numbers)
    min_result = int(1e8)
    max_result = int(-1e8)

    calculate(1, numbers[0], add, sub, mul, div)
    print(f'#{t} {max_result-min_result}')




