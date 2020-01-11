# What are Priority Queues? (not the same as a heap!!!)
- an Abstract Data Type meaning it can be implemented with other data structures
- This is similar to a queue except every element has a certain priority
- Elements with higher priority come out of priority queue first
- PQ only support elements that are comparable! 
    - Things inserted must be ordered in some way so we can assign priorities
    - Smaller numbers will be removed from PQ first (higher priority)
- An ordered sequence is not guaranteed

- <b>Poll</b> removes element with highest priority in PQ
- <b>Add</b> adds element into the PQ

- A PQ knows which element to poll next (highest priority) because it uses a HEAP (value of parent node is always >= child nodes)

## When do we use it?
- Dijkstra's Shortest Path Algorithm
- When you want to dynamically fetch the next best or next worst element
- Huffman coding
- Best First Search algorithms such as A* --> continuously grab the next most promising node
- Minimum Spanning Tree Algorithms

## Complexities
- Construction O(N)
- Polling O(logN) because you need to restore the heap invariant
- Peeking O(1)
- Adding O(logN) because you may need to reshuffle the heap by bubbling up the value
- Removing an element that is not the root element is O(N) [usually not used]
    - Advanced removing with a hash table O(logN)
- Checking if it contains the item naive is O(N) - just scan through all the elements
    - With a hashtable, you can do it in O(1)