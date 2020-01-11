# doesn't work!
 swap(my_str, i, j):
    my_str = list(my_str) # find another way to turn into list
    temp = my_str[i]
    my_str[i] = my_str[j]
    my_str[j] = temp
    my_str = str(my_str)
    return my_str

def calculateAux(my_str, left, right):
    if left == right:
        print(my_str)
    else:
        i = 0
        while  i <= right:
            swapped = swap(my_str, left, i)
            i += 1

def calculate(my_str, left, right):
    return calculateAux(my_str, 0, len(my_str) - 1)
    
test = 'ABC'
print(calculate(test, 0, len(test)))
