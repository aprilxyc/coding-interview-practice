def check_permutation(word1, word2):
    if len(word1) != len(word2):
        return False
    if sorted(word1) == sorted(word2):
        return True
    return False

print(check_permutation("hello", "ohelle"))