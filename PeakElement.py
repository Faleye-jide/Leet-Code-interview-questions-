lst = [1, 2, 3, 7, 6, 5]

# linear approach
def findPeak(lst):
    if len(lst) == 1:
        return 0
    n = len(lst)
    peak = 0
    if lst[0] > lst[1]:
        return lst[0]
    if lst[n-1] > lst[n-2]:
        return lst[n-1]


    for i in range(1, n-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            return i
    return -1 # there is no peak element

print(findPeak(lst))


# binary search approach