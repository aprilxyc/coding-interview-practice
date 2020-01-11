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

# my own solution 11/01 (improved but struggles with remember to use .keys() and .values() for dictionary - would've made life so much easier if I remembered
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        stud_scores = {} #{1: [91], 92}
        for i in items: 
            if i[0] not in stud_scores: #[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
                stud_scores[i[0]] = [i[1]] # 
            else:
                stud_scores[i[0]].append(i[1])
        
        result = []
        for i in stud_scores.keys():
            individual_score = stud_scores[i]
            individual_score.sort(reverse=True)
            average = sum(individual_score[:5]) // 5
            result.append([i, average])
        
        return sorted(result)

# correct data structure to use for this to make it faster is a priority queue
# using a priority queue limits it to 5 ids
# explanation of complexity:
# https://leetcode.com/problems/high-five/discuss/350178/is-complexity-n-log-5
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        dic = {}      
        for idx,score in items:
            if idx in dic:
                h = dic[idx]
                if len(h) < 5:
                    heapq.heappush(h, score)
                else:
                    heapq.heappushpop(h, score)
            else:
                h = [score]
                heapq.heapify(h)
                dic[idx] = h
                
        return [[idx, sum(res)//len(res) ] for idx, res in dic.items()]

