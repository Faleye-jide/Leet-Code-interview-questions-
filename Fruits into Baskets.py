"""
Given an array of characters where each character represents a fruit tree,
you are given two baskets, and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.
"""
from collections import defaultdict
def fruits_into_baskets(fruits):
    window_start = 0
    fruit_count = 0
    fruits_dict = defaultdict(int)

    for window_end in range(len(fruits)):
        fruit = fruits[window_end]
        fruits_dict[fruit] += 1

        while len(fruits_dict) > 2:
            fruit = fruits[window_start]
            fruits_dict[fruit] -= 1
            if fruits_dict[fruit] == 0:
                del fruits_dict[fruit]
            window_start += 1

        fruit_count = max(fruit_count, window_end - window_start + 1)
    return fruit_count


Fruit = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(Fruit))


