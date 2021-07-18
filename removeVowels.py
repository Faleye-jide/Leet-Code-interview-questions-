input = "leetcodeisacommunityforcoders"
import time
start = time.time()
# linear approach
def removeVowels(input):
    vowels = ["a","e","i","o","u"]
    res = ""
    for char in input:
        if char not in vowels:
            res += char
    return res
stop = time.time()
print(removeVowels(input))
print(stop)


# set dictionary
import time
start = time.time()
def removeVowels(input):
    vowels = set()
    vowels.add("a")
    vowels.add("e")
    vowels.add("i")
    vowels.add("o")
    vowels.add("u")
    res = ""

    for char in input:
        if char not in vowels:
            res += char

    return res
stop = time.time()
print(removeVowels(input))
print(stop)