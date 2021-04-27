num_friends = [2,3,5,7,8]

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:  # if odd, return middle number
        return sorted_v[midpoint]
    else:
        low = midpoint - 1
        high = midpoint
        return (sorted_v[low] + sorted_v[high]) / 2

print(median(num_friends))