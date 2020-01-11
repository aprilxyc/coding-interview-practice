def is_unique(word):

    is_unique_counter = {}
    #hello
    for letter in word:
        if letter not in is_unique_counter: # {l : 1}
            is_unique_counter[letter] = 1
        else: # {h : 1 }
            is_unique_counter[letter] += 1 #{l : 2}
            return False
    return True

print(is_unique("helo"))



