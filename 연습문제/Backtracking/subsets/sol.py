def backtrack_subsets(nums, idx, current, result):
    if idx == len(nums):
        result.append(current[:])
        return
    
    backtrack_subsets(nums, idx+1, current, result)

    current.append(nums[idx])
    backtrack_subsets(nums, idx+1, current, result)
    current.pop()

nums = [1, 2, 3]
result = []
backtrack_subsets(nums, 0, [], result)
print(result)