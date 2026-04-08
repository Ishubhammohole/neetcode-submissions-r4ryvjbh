class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for num in hashset:
            if num - 1 not in hashset:
                current = num
                streak = 1

                while current + 1 in hashset:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest




        
        