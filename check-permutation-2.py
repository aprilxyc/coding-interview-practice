def check_permutation(word1, word2):

    if len(word1) != len(word2):
        return False
    
    char_count = {}
    for letter in word1:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    for letter in word2:
        if letter in word2:
            char_count[letter] -= 1
        if char_count[letter] < 0:
            return False
    return True
    
    
print(check_permutation("racecar", "aaccerr"))

    
