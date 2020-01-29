"""
https://leetcode.com/problems/employee-importance/
"""

# QUEUE FOR BFS GRAPH PROBLEMS
# STACK FOR DFS GRAPH PROBLEMS

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

import collections
class Solution:
    def getImportance(self, employees: List['Employee'], target_id: int) -> int:
        # Deal with the case where null inputs are possible
        if employees == []:
            return 0
        
        # Create a hashtable where the key is the ID and value is the Employee object itself
        hashtable = {}
        res = 0
        for node in (employees):
            if hashtable.get(node.id) == None:
                hashtable[node.id] = node
            
        # Queue will only contain the worker IDs and we will reference the respective object via O(1) calls w/ the hashtable
        queue = collections.deque([target_id])
        while queue:
            worker_id = queue.popleft()         #Grab employee ID
            worker = hashtable.get(worker_id)   #Grab employee object
            worker_importance = worker.importance #Use employee object to get the employee's importance
            res += worker_importance
            
            for ids in (worker.subordinates): #Check if the employee has subordinates
                queue.append(ids)
            
        return res
		
