from itertools import combinations

def find_invalid_num(nums, p=25):
    for i, num in enumerate(nums[p:], p):
        if all(a + b != num for a, b in combinations(nums[i-p:i], 2)):
            return num


assert find_invalid_num([int(x) for x in open('input-09.txt')]) == 556543474


def find_weakness(raw_data, p=25):
    nums = [int(x) for x in raw_data]
    invalid_num = find_invalid_num(nums, p)
    for i, start_num in enumerate(nums):
        visited = [start_num]
        for end_num in nums[i+1:]:
            visited.append(end_num)
            run_sum = sum(visited)
            if run_sum == invalid_num:
                return min(visited) + max(visited)
            if run_sum > invalid_num:
                break


assert find_weakness(open('input-09.txt')) == 76096372
