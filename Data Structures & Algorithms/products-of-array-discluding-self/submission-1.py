class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        suffix = 1

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix = suffix * nums[i + 1]
            output[i] = suffix * output[i]

        return output
        