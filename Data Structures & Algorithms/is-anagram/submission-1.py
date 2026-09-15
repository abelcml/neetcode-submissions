class Solution: # sort? # dict?
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # # O(nlogn)
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)

        # for i in range(len(s_sorted)):
        #     if s_sorted[i] != t_sorted[i]:
        #         return False
        
        # return True

        # O(n)
        count = [0]*26
        for i , j in zip(s,t):
            count[ord(i) - ord('a')] += 1
            count[ord(j) - ord('a')] -= 1

        return all (x== 0 for x in count)

        