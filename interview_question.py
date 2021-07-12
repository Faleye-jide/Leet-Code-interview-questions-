# def remove_duplicate(nums):
#     n = len(nums)
#
#     for i in range(n):
#         for j in range(i+1, n-1):
#             if nums[j] != nums[i]:
#                 nums[j] = nums[i]
#                 j+=1
#         i+1
#
#     return j-1
#
# num = [2, 3, 3, 3, 6, 9, 9]
# print(remove_duplicate(num))




def pair_sum(arr, target_sum):
    n = len(arr)
    left, right = 0, n-1

    while left<=right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:
            return [left, right]

        if target_sum > cur_sum:
            left+= 1

        else:
            right-= 1
    return  [1, -1]

Input = [1, 2, 3, 4, 6]
target_sum =6
print(pair_sum(Input, target_sum))


