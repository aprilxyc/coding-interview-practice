def toLowerCase(str):
    # O(N) where N is the length of the input string

    # using mathematical relationship of ASCII values
    new_string = ""
    for i in range(len(str)): # loop through the word
        print(ord(str[i]))
        if 65 >= ord(str[i]) >= 90:
            new_string += chr(ord(str[i]) + 32)
        else:
            new_string += str[i].lower()
    return new_string

print(toLowerCase("hello"))

# LeetCode one-liners with advanced Python
def toLowerCase(self, str): 
    # thing you want to do, the if statement, FOR whatever in whatever
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)