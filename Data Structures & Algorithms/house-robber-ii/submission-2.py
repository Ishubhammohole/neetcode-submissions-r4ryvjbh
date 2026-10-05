class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def helper(houses):
            if len(houses) == 1:
                return houses[0]
            dp0 = houses[0]
            dp1 = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                result = max(houses[i] + dp0, dp1)
                dp0 = dp1
                dp1 = result
            return dp1
            
        A = helper(nums[1:])
        B = helper(nums[:-1])

        return max(A, B)
        
        
        