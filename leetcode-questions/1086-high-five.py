class Solution(object):
    # https://leetcode.com/problems/high-five/discuss/464841/Python-solution-with-hash
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        stud_scores = {}
        for i in items: # go through the items
            if stud_scores.get(i[0]): # if the value exists 
                stud_scores[i[0]].append(i[1]) # append it to the list that exists in the value already
            else:
                stud_scores[i[0]] = [i[1]] # otherwise let it equal the value
                
        for i in stud_scores.keys(): # go through the keys
            stud_scores[i].sort(reverse=True)
            stud_scores[i] = stud_scores[i][0:5]
        
        stud_avg = {}
        for i in stud_scores.keys():
            stud_avg[i] = sum(stud_scores[i]) //5
            
        stud_list = []
        for i in stud_scores.keys():
            stud_list.append(i)
            stud_list.sort()
            
        return [[i, stud_avg[i]] for i in stud_list]