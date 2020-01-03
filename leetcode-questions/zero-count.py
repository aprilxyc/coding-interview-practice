# This problem is taken from V. Anton Spraul's Think Like a Programmer

# Write a recursive function that calculates how many 0's there are in an array

# My solution
def zeroCountRecursive(num_arr, size):
    lastElem = 0
    if size == 0:
        return 0
    if num_arr[size - 1] == 0:
        lastElem = 1
    total = zeroCountRecursive(num_arr, size - 1) + lastElem
    return total

print(zeroCountRecursive([0, 0, 1, 0, 2], 5))

# better solution 
int zeroCountRecursive(int numbers[], int size) {
 if (size == 0) return 0;
 int count = zeroCountRecursive(numbers, size - 1);
 if (numbers[size - 1] == 0) count++;
 return count;
}