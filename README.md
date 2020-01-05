# Algorithms & Data Structures (with Python)
Reminding myself that I am not naturally great at this but all it takes is practice, dedication and hard work. I made this repository to help me keep track of some of the questions / solutions I have done (mainly LeetCode).

### PROBLEMS COMPLETED:
** Note the [x] keeps track of whether I have revised them
#### Easy:
24/12
- [ ] 760
- [ ] 1266 [https://leetcode.com/problems/minimum-time-visiting-all-points/discuss/436317/python-3-Easy-peasy-lemon-squeezy]
- [ ] 1221
- [ ] 1119
- [ ] 1295
- [ ] 771
- [ ] 1290
- [ ] 938 [https://www.youtube.com/watch?v=FMFytleZRWA]

25/12
- [ ] 1252 [https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/discuss/456746/python3-simple-and-memory-saving-solution]

30/12
- [ ] 1134 [https://leetcode.com/problems/armstrong-number/discuss/455073/Python-3-90] (
(Good solution demonstrating use of list comprehensions)[https://leetcode.com/problems/armstrong-number/discuss/455393/Python3-One-liner-beats-98]
- [ ] 1213 Intersection of Two Arrays

03/01
- Think Like a Programmer (V. Anton Spraul) Recursion Problems
- [ ] 1086
- [ ] 1299
- [ ] 344 (easy problem to learn to optimise)
- [ ] 136 (study XOR bitwise operators and how it works)

05/01
- [x] 412 FizzBuzz
- [x] 104 Max Depth of Binary Tree
- [x] 206 Reverse Linked List
- [x] 237 Delete Node in a Linked List
- [x] 203 Move Zeroes [https://leetcode.com/problems/move-zeroes/discuss/391025/2-methods-for-python-simple-code]
^ Study this method too: https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.
- [x] 169 Majority Element STUDY [https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).]
- [x] 242 Valid Anagram STUDY these solutions [https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).]
- [ ] 217 Contains Duplicate


### My Learnings:
- use %10 to get the last digit
- use //10 to get the whole number without hte last digit 
- for the two above points, loop it until != 0
- *=2 is same as <<=1
- use list comprehension with joins
- use multiple pinters
- useful to use enumerate in Python
- head recursion is where the recursive call comes BEFORE other processing in the function (recursive call happens before the other processing)
- tail recursion is where the processing occurs BEFORE the recursive call - recursive call is the last step in the function (recursive call is postponed until the end)
- if you set("aabc"), you get {a, b, c} (useful in finding distinct characters) [https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/]
- use the functions for dictionarys i.e. .keys() returns the keys in an object e.g. 
        for i in dictionary.keys():
            print(i)
    - use .get() to get the value of the respective key you are getting
- make use of being able to traverse Python backwards easily e.g. (len(aList) - 1, -1, -1)
- make use of XOR and reduce for linear time array questions (bitwise solution) [problem 136]
- Remember you can use XOR (bitwise operators) and with the case of XOR, you can XOr in any order and it will be the same as long as you XOR all the elements.
i.e. a XOR b = b XOR a
(a XOR b) XOR c == a XOR (b XOR c) returns the same thing. Hence if you had [4, 1, 2, 1, 2], 1 XOR 1 will cancel out to 0, 2 XOR 2 will cancel out to 0 and 4 will be the only number left so we know that that is the number that is different. 
- Be careful with Binary Trees: 1) they don't have to be balanced 2) You don't need a while loop to iterate through it if you already are already recursively going through the tree. For this particular question, I only need to check whether the root exists or not: [https://leetcode.com/problems/maximum-depth-of-binary-tree/]
- in a Linked List question, be careful of your loop constraint i.e. while current.next is not None or while current is not None [in reversing a list, we only need to know about the current]
- when asked to delete an entry from a linked list without the head, you CANNOT delete it. You can only copy the values from the next part of the linked list into where it is now (overwrite it)
- use a lag variable if you have two pointers and need to replace or move something
- make use of the count function to find how many times something appears
- remember to use the SET function for questions containing duplicates in an array or similar

#### Struggles with Recursion
(This chapter really helped) [https://nostarch.com/download/samples/TLAP_ch6.pdf]
The first thing about recursion is DO NOT THINK about all the steps in recursion. This is the Big Recursive Idea!
