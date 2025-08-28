def backtrack_permutations(nums, used, current, result):

    # 만약 마지막 자리까지 갔으면 result에 추가 
    if len(current) == len(nums):
        result.append(current[:])
        return 

    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            current.append(nums[i])

            backtrack_permutations(nums, used, current, result)

            # 백트래킹(원상 복구)
            current.pop()
            used[i] = False

nums = [1, 2, 3]
used = [False] * len(nums)
result = []
backtrack_permutations(nums, used, [], result)
print(result)
