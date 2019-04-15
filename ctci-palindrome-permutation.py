def palindrome_permutation(string):
    """ Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or
    phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not
    need to be limited to just dictionary words.
    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco cta", etc...
    :time complexity: O(n) where n is the number of letters in the word
    :space complexity: O(n) where n is the length of the word
    """
    # remove spaces by replacing them with ""
    string = string.replace(" ", "")

    dictionary = {}
    for i in string:

        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1


    odd_counter = 0  # keeps track of the num of words wtih 1 appearance
    for i in dictionary:
        # check condition
        if dictionary[i] % 2 != 0: # if it is odd, then increment
            odd_counter += 1

        # if there is > 1 odd, then not palindrome
        if odd_counter > 1:
            return False

    return True

if __name__ == "__main__":
    print(palindrome_permutation("aabbccbbaa"))


