class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ## could be [1 , 56789 , 2]
        ## 理想情況下，計算 hash 並索引陣列是一個常數時間操作，所以查找/插入/刪除平均為 O(1)。


        # pop 
        # sort 
        # count += 1

        all_elements = set(nums)

        if not nums:
            return 0
        for i in nums:
            if (i+1 in all_elements) or (i-1 in all_elements) :
                pass
            else:
                nums.remove(i)

        nums.sort()


        count = 1
        max_count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[i] == nums[i-1]:
                pass
            else:
                count = 1
        
        return max_count

        