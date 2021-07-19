nums = [0, 1, 2, 4, 5]

def missing_number(nums):
    new_set = set()
    for i in nums:
        new_set.add(i)
    print(new_set)
    for i in range(len(nums)):
        if i not in new_set:
            return i
    return -1

print(missing_number(nums))