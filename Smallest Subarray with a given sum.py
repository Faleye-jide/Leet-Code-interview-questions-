"""
Given an array of positive numbers and a positive number ‘S,’
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists
"""
"""
Algorithm:
1. add the elements from the begining of the array until its sum 
is greater or equal to s
2. these elements would be our window constituents then find the smallest 
length that makes our window greater or equal to s
3. keep moving the window ahead by adding one element 
4. At each step, we would want to shrink the windom from the begining 
until the window sum is less than s. the intent is to find the smallest length
    ...check if the current length is the minimum, then keep it 
    ... subtract the first element of the windom from the window sum
"""
import math
def smallest_subarray_with_given_sum(s, arr):
    window_sum, window_start = 0, 0
    min_length = math.inf

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            cur_length = window_end - window_start + 1
            min_length = min(min_length, cur_length)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length
s, Input = 7, [2, 1, 5, 2, 3, 2]
print(smallest_subarray_with_given_sum(s, Input))

