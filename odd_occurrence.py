def oddOccurence(arr):
#     for i in range(len(arr)):
#         count = 0
#         for j in range(i, len(arr)):
#             if arr[i] == arr[j]:
#                 count=+1
#
#         if count % 2 != 0:
#             print(arr[i])
#             break
#
# arr = [8, 3, 6, 4, 5, 6, 4, 3, 5, 2, 4, 4, 2]
# print(oddOccurence(arr))


# dictionary

#     dict = {}
#     for i in range(len(arr)):
#         if i in dict:
#             [dict[arr[i], i]]
#         else:
#             dict[arr[i]] = 1
#
#     return dict
#
# arr = [8, 3, 6, 4, 5, 6, 4, 3, 5, 2, 4, 4, 2]
# print(oddOccurence(arr))

# XOR approach
    res = 0
    for element in arr:
        res = res ^ element

    return res

arr = [8, 3, 6, 4, 5, 6, 4, 3, 5, 2, 4, 4, 2]
print(oddOccurence(arr))