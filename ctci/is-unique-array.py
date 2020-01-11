def is_unique(word):
    is_unique_array = []
    flag = True
    for letter in word:
        if letter in is_unique_array:
            return False
        else:
            is_unique_array.append(letter)
    return True

print(is_unique("april"))
        