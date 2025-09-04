import sys
import itertools

sys.stdin = open('input.txt', 'r')

def inspect_run(ls):
    ls.sort()
    if ls[0] == ls[1] -1 and ls[1] == ls[2] -1:
        return True
    return False 

def inspect_triplet(ls):
    if ls[0] == ls[1] and ls[1] == ls[2]:
        return True
    return False 

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().strip()))

    answer = False

    for subset in itertools.permutations(numbers, 6):
        now_ls1 = list(subset[:3])
        now_ls2 = list(subset[3:])
        if inspect_run(now_ls1) and inspect_triplet(now_ls2):
            answer = True
            break
        elif inspect_triplet(now_ls1) and inspect_triplet(now_ls2):
            answer = True
            break
        elif inspect_run(now_ls1) and inspect_run(now_ls2):
            answer = True
            break
        elif inspect_triplet(now_ls1) and inspect_run(now_ls2):
            answer = True
            break

    print(f'#{t} {answer}')


