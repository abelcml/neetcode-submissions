from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        groups = defaultdict(int)

        for num in nums:
            groups[num] += 1

        inv_groups = defaultdict(list) 

        for key, value in groups.items():
            inv_groups[value].append(key) ##{3 :[1,2]  , 4: [5,7] , 1 : [2] }

        # inv_groups.sort()  WRONG !!
        # L = list(inv_groups.values())
        # print(L)
        # flattened = [item for sublist in L for item in sublist]

        # return flattened[-k:]
        
        frequencies = sorted(inv_groups.keys())

        flattened = []

        for freq in frequencies:
            flattened.extend(inv_groups[freq])

        return flattened[-k:]