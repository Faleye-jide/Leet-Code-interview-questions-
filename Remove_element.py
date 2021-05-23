def remove_element(arr, key):
    element = 0
    n = len(arr)
    for i in range(n):
        if arr[element] != key:
            arr[element] = arr[i]
            i+=1
    return element

Input = [1, 2, 3, 6, 8, 10, 9, 4]
Key = 3
print(remove_element(Input, Key))


# def remove_element(arr, key):
#     i = 0
#     for j in range(len(arr)):
#         if arr[i] != key:
#             arr[i] = arr[j]
#             j+=1
#     return
#
# Input = [1, 2, 3, 6, 8, 10, 9, 4]
# # Key = 3
# # print(remove_element(Input, Key))
