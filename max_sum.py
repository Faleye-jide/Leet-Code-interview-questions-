def max_sum(arr):
    cur_sum = 0
    for num in range(1, len(arr)):
        if cur_sum < arr[num]:
            cur_sum = arr[num]
        else:
            num+=1

    return cur_sum

number = [1,3,4,5,6]
print(max_sum(number))