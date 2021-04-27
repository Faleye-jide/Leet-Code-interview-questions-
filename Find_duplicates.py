# def duplicates(arr):
#     if arr is None:
#         return
#
#     for i in range(0,len(arr)-1):
#         if arr[i] == arr[i+1]:
#             return True
#         i+=1
#
#     return False
# number = [1,1,3,4,5,6,7]
# print(duplicates(number))

# set approach
def duplicates(arr):

    for i in arr:
        if len(arr) == len(set(arr)):
            return True
    return False
number = [1,1,3,4,5,6,7]
print(duplicates(number))