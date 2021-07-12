lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

# loop method
result = []
for num in lst1:
    if num in lst2:
        result.append(num)
print(result)


# set
def intersection(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    for num in set1:
        if num in set2:
            return set1.intersection(set2)
print(intersection(lst1, lst2))