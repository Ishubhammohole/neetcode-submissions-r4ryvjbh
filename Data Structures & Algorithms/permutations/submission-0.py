class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                cur.append(nums[i])
                used[i] = True

                backtrack(cur)

                cur.pop()
                used[i] = False
        backtrack([])
        return res

        