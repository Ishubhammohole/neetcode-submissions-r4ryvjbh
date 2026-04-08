class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index, num in enumerate(nums):
            complement = target - num

            if complement in my_map:
                return [my_map[complement], index]
            my_map[num] = index


        