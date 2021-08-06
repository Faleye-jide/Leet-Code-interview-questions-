"""
Given a string and a pattern,
find out if the string contains any permutation of the pattern.
permutation is defined as the re-arranging of the characters of the string
"""
String="oidbcaf"
Pattern="abc"
def find_permutation(str, pattern):
    window_start = 0
    matched = 0
    pattern_freq = {}
    for char in pattern:
        if char not in pattern_freq:
            pattern_freq[char] = 0
        else:
            pattern_freq[char] += 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in pattern_freq:
            pattern_freq[right_char] -= 1
            if pattern_freq[right_char] == 0:
                matched += 1

        if matched == len(pattern_freq):
            return True

        if window_end >= len(pattern - 1):
            left_char = str[window_start]
            window_start += 1
            if left_char in pattern_freq:
                if pattern_freq[left_char] == 0:
                    matched -= 1
                    pattern_freq[left_char] +=

