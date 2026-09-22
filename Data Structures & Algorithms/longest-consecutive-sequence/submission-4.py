class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ## could be [1 , 56789 , 2]
        ## 理想情況下，計算 hash 並索引陣列是一個常數時間操作，所以查找/插入/刪除平均為 O(1)。


        # pop 
        # sort 
        # count += 1
        
        '''
        all_elements = set(nums)

        if not nums:
            return 0

        # for i in nums:
        #     if (i+1 in all_elements) or (i-1 in all_elements) :
        #         pass
        #     else:
        #         nums.remove(i)   this will result in O(n^2)

        nums.sort()  ## sort is still O(nlogn)


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
        '''

        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:          # x 是某段序列的起點
                length = 1
                while x + length in s:
                    length += 1
                best = max(best, length)
        return best
        