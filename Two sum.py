def twoSum(arr, target):
    for i in range(len(arr)):
        a = arr[i]
        for j in range(i, len(arr)):
            b = arr[j]
            sum = a + b
            if sum == target:
                return [i,j]

number = [1,3,4,5,6]
output = 8
print(twoSum(number, output))

# dictionary approach

def twoSum(arr, target):
    dict = {}
    for num in range(len(arr)):
        complement = target - arr[num]
        if complement in dict:
            return [dict[complement],num]
        else:
            dict[arr[num]] = num

number = [1,3,4,5,6]
output = 10
print(twoSum(number, output))