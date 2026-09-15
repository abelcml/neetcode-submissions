class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = set()
        for i in range(0,len(nums)):
            if nums[i] not in S:
                S.add(nums[i]) 
            else:
                return True
            
        return False