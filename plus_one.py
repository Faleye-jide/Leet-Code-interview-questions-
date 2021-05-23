def plusOne(digits):
# create an empty string
# loop over the digits and convert the number to int, increment the number
# create a new list and append the int number.
    num = ''
    for i in digits:
        num += str(i)
    num = int(num)
    num +=1
    num = str(num)
    ans = []
    for i in num:
        ans.append(int(i))
    return ans

digits = [5, 3, 2, 4]
print(plusOne(digits))