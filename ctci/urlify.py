def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)
    print(new_index)
    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_in ex - 1] = string[i]
            new_index -= 1

    return string

urlify("Mr John Smith   ", 13)