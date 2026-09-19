class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)
        
        for num in nums:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1
                while cur_num + 1 in num_set:
                    cur_num = cur_num + 1
                    cur_length += 1
                max_length = max(max_length, cur_length)
        return max_length

        