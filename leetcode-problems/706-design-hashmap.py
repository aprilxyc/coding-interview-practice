"""
https://leetcode.com/problems/design-hashmap/
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.items[key + 1] = value # accounting for index 0
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.items[key + 1] < 0:
            return -1
        return self.items[key + 1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.items[key + 1] > 0:
            self.items[key + 1] = -1 # remove the mapping by setting it to negative
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)