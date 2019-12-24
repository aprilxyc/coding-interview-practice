def balancedStringSplit(self, s: str) -> int:
    # O(N) where N is the number of characters in the string
    split_count = 0 # keep track of the output (max num of split balanced strings)
    counter = 0 # keeps track of the number of R's and L's we're on
    for i in s: # loop through the string of R's and L's
        if i == 'R':
            counter += 1 # increment if R
        if i == 'L': # decrement if L
            counter -= 1
        if counter == 0:
            split_count += 1
    return split_count


        