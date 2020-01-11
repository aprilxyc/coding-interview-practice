"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
"""
# think of the 1 in our decimal system when we add as 26. So whenever we see a new column, we simply need to multiply it by 26. 
# in this case, the rightmost column is the ones column

# perform subtraction fo ordinal values to get hwo far away the character is from A

# this is doing it in the reverse
def titleToNumber(s):
    result = 0
    x = 0
    for char in s[::-1]:
        # get how far away the letter is from A 
        # multiply it by 26 ** x 
        result += (ord(char) - ord('A') + 1) * 26 ** x 
        x += 1
    return result

# doing it not in the reverse
# make it so that the column starts at the end
def titleToNumber(s):
    result = 0
    x = len(s) - 1
    for char in s[::-1]:
        result += (ord(char) - ord('A') + 1) * 26 ** x
        x += 1
    return result