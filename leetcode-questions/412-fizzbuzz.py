def fizzBuzz(self, n: int) -> List[str]:
    #O(N) time complexity where N is the number of elements in n
    # O(N) space complexity where N is the number of elements in n
    complete_list = []

    i = 1
    while i < n + 1: # check index later
        if i % 3 == 0 and i % 5 == 0:
            complete_list.append("FizzBuzz")
        elif i % 3 == 0:
            complete_list.append("Fizz")
        elif i % 5 == 0:
            complete_list.append("Buzz")
        else:
            complete_list.append(str(i))
        i += 1
    return complete_list
# note that the for loop is faster in this case?
# can also use a for loop
https://leetcode.com/problems/fizz-buzz/discuss/464163/My-Solution%3A-Python-Simple-O(n)-Time-Complexity-Beats-97