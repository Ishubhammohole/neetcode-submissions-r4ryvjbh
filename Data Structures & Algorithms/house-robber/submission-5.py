class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, n):
            result = max(nums[i] + dp0, dp1)
            dp0 = dp1
            dp1 = result

        return dp1
        
        