from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) # {key =  : value = []}
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1 # [ 1, 0 , ..... ,2 ..... 0, 1]
            groups[tuple(count)].append(s) # {key = ( 1, 0 , ..... ,2 ..... 0, 1) : ["azcaskjn" , "..."]}
            
            # if key not in groups:
            #     groups[key] = []
            # groups[key].append(s)
                        

        return list(groups.values())


        # original thought 
        # for word in strs , for ch in word , D[ord("i")] += 1
        # store every word to unique dict, then check if there are identical dict?
        
        # sort by len before print

        # D = {}

        # for i , word in enumerate(strs):
        #     subD = defaultdict(int)
        #     for ch in word:
        #         subD[ch] += 1   #  dict should init 
            
        #     D[i] = subD
        

        # L = [] 

        # for i in D:
        #     placed = False
        #     for subL in L:
        #         if D[i] == D[subL[0]]:
        #             subL.append(i)
        #             placed = True
        #             break
        #     if not placed:
        #         L.append([i])  #[[0,1,3], [2,4], [5]]
        


        # ans = []

        # for subL in L:
        #     ans.append([strs[i] for i in subL])

        # return ans
