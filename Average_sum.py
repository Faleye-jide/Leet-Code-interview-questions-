"""
Given an array, find the average of all contiguous
subarrays of size ‘K’ in it.
"""
"""
Approach: sliding window 0(N) time and space complexity
Algorithm:
1. instantiate two variables and assigned to zero
2. Add element till the window get to the required window size k
3. calculate the average from the sum of the window size 
4. slide the window by one element to move to the next subarray 
5. return the result
"""
def find_averages_of_subarrays(K, arr):
    window_start, window_sum = 0, 0
    result = []
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K - 1:
            result.append(window_sum/K)
            window_sum -= arr[window_start]
            window_start += 1

    return result

K, Array = 5, [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(find_averages_of_subarrays(5, Array))

"""
Brute force:
1. calculate the sum of the five element subarray of the array
2. divide the sum K to get the average of each subarray
"""

def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr) - K+1):
        curSum = 0
        for j in range(i, i+K):
            curSum += arr[j]
        result.append(curSum/K)
    return result
print(find_averages_of_subarrays(5, Array))