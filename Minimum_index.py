def indexOfMin(list):
    minIndex = 0
    currentIndex = 1
    n = len(list)

    while currentIndex < n:
        if list[currentIndex] < list[minIndex]:
            minIndex = currentIndex
        else:
            currentIndex += 1

    return minIndex

num = [2,3,4,1,7,9]

print(indexOfMin(num))


# alternative solution

def indexMin(list):
    minIndex = list[0]
    n = len(list)


    for i in range(1, n):
        if list[i] < list[minIndex]:
            minIndex = list[i]
        i += 1

    return minIndex

num = [2,3,4,1,7,9]

print(indexOfMin(num))
