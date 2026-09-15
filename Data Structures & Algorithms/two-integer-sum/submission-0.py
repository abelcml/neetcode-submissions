class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # sol1
        # for i , for j , but O(n^2)

        # sol2
        seen = {}
        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen:
                return [seen[diff],i]
            
            if nums[i] not in seen:
                seen[nums[i]] = i