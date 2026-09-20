class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # result = []
        # for i in range(len(nums)):
        #     L_compute = nums[:i] + nums[i+1:]

        #     x = 1
        #     for i in L_compute:
        #         x = x*i

                
        #     result.append(x)
        # return result

        n = len(nums)
        result = [1] * n

        # 第一趟：result[i] 存 i 左邊的乘積
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # 第二趟：從右往左，乘上 i 右邊的乘積
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        