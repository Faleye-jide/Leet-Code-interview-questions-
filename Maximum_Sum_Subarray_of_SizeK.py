"""
Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’.
"""
"""
Bruteforce 0(N*K) Time and 0(N) space
1. find the sum of all possible k sized subarray in the given array 
2. find the subarray with the highest sum and return it 
"""
k, input = 3,  [2, 1, 5, 1, 3, 2]
def max_sub_array_of_size_k(k, arr):
    maxSum = 0
    for i in range(len(arr) - k+1):
        curSum = 0
        for j in range(i, i+k):
            curSum += arr[j]
            maxSum = max(curSum, maxSum)
    return maxSum

print(max_sub_array_of_size_k(k, input))

"""
Better Approach: sliding window 0(N) time and 0(1) space
1. Add element till the subarray get to the required k
2. if the sum of the subarray does not equal the output, slide the window by 
one element to right and reducing the starting point 
3. calculate the sum and compare with previous 
4. repeat step 3 till you get the max subarray in the array
"""
def max_sub_array_of_size_k(k, arr):
    window_sum, maxSum = 0, 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            maxSum = max(window_sum, maxSum)
            window_sum -= arr[window_start]
            window_start += 1
    return maxSum

print(max_sub_array_of_size_k(k, input))
