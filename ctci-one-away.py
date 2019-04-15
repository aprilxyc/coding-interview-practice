""" ctci q1.5
There are three types fo edits that can be performed on strings: insert a character, remove a chracter, or replace a
character. Given two strings, write a function to check if they are one edit (or zero edits) away.
example
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false"""

def one_away(A, B):

    if A == B: # same word
        return True

    arr = [0] * 128 # crreate array of the ASCII values

    for i in range(len(A)):
        index = ord(i)
        

if __name__ == "__main__":
    print(one_away("pale", "ple"))