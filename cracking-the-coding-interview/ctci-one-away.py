""" ctci q1.5
There are three types fo edits that can be performed on strings: insert a character, remove a chracter, or replace a
character. Given two strings, write a function to check if they are one edit (or zero edits) away.
example
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false"""

def one_away(A, B):

    A_len = len(A)
    B_len  = len(B)
    max_word = max(A_len, B_len) # get the max word

    first_index = A[0] # get first index
    last_index = A[len(A)] # get last index

    # insertions and replacements
    diff_index = 0
    for i in range(len(max_word)): # go through the first word
        if A[i] == B[i]:
            continue
        else:
            diff_index += 1

    for i in range(len(max_word)):
        if i
        pass
        #do stuff here

    for j in range(len(max_word), 0, -1):
        pass

    # deletions

    if diff_index > 1:
        return False
    return True



if __name__ == "__main__":
    # print(one_away("pale", "ple"))
    A = "april"
    B = "jason"
    print(max(A, B))