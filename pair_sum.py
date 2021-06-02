arr = [8, 7, 2, 5, 3, 1]
sum = 10

# brute force approach 0(N^2) time and 0(1) space
#
# def findPair(arr, sum):
#     if len(arr) <= 0:
#         return 0
#
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == sum:
#                 return (arr[i] , arr[j])
#
#     return -1

# print(findPair(arr,sum))

# sorting approach nlogn time and 0(1) space
# def findPair(arr, sum):
    # if len(arr) <= 0:
    #     return 0
    # arr.sort()
    #
    # low, high = 0, len(arr) - 1
    #
    # while low < high:
    #     if arr[low] + arr[high] == sum:
    #         return (arr[low], arr[high])
    #     # if the pair sum is less than the target sum, increment low
    #     # if the pair sum is greater than the target sum, decrement high
    #     # if the pair sum equals target sum, return both index
    #     if arr[low] + arr[high] < sum:
    #         low = low + 1
    #     else:
    #         high = high - 1
    # return -1
#
# print(findPair(arr, sum))


# dictionary 0(N) time and 0(N) space
def findPair(arr, sum):
    dict = {}
    for num in range(len(arr)):
        compliment = sum - arr[num]
        if compliment in dict:
            return (arr[dict[compliment]], arr[num])
        else:
            dict[arr[num]] = num

print(findPair(arr, sum))

#     dict = {}
#     for i, v in enumerate(arr):
#         comp = sum - v
#         if comp in dict:
#             return (arr[dict[comp]], arr[i])
#         else:
#             dict[v] = i
#
# print(findPair(arr, sum))