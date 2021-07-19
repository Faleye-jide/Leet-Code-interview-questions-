nums = [1, 2, 3, 3, 1]

def singleNumber(nums):
    new_set = set()
    for i in nums:
        if i not in new_set:
            new_set.add(i)
        else:
            new_set.remove(i)

    for i in new_set:
        return i

print(singleNumber(nums))