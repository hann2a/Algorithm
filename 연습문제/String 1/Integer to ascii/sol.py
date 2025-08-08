def itoa(integer_value):

    # 0은 0으로 
    if integer_value == 0:
        return '0'
    
    # 음수는 양수로 
    is_negative = (integer_value < 0)
    if is_negative:
        integer_value = -integer_value

    # 나머지는 문자로 누적 
    result_str = ''
    while integer_value > 0:
        remainder = integer_value % 10 
        result_str = chr(48+remainder) +result_str
        integer_value //=10

    if is_negative:
        result_str = '-' + result_str
    return result_str 

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    result = itoa(number)
    print(f'#{test_case} {result}', type(result))

