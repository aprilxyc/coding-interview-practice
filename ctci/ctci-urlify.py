# problem 1.3 ctci
""" Write a method to replace all spaces in a string with %20. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given
the 'true' length of the string.
E.g.
Input: 'Mr John Smith     ", 13
Output: 'Mr%20John%20Smith'
"""

def urlify(string, str_len):
    total_len = len(string)
    num_spaces = total_len - str_len
    final_index = total_len - num_spaces

    complete_word = string[0:final_index]
    for i in complete_word:
        complete_word = complete_word.replace(" ", "%20")
    complete_word = complete_word + "%20"
    return complete_word

if __name__ == "__main__":
    print(urlify("Mr John Smith     ", 13))
