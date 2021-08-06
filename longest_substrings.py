"""
Given a string, find the length of the longest substring in it
with no more than K distinct characters.
"""
Input, K = "araaci", 2
from collections import defaultdict
def longest_substring_with_k_distinct(str1, K):
    max_length = 0
    window_start = 0
    char_set = defaultdict(int)

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        char_set[right_char] += 1

        while len(char_set) > K:
            left_char = str1[window_start]
            char_set[left_char] -= 1
            if char_set[left_char] == 0:
                del char_set[left_char]
            window_start += 1

        max_length = max(max_length , window_end - window_start + 1)
    return max_length


print(longest_substring_with_k_distinct(Input, K))


