class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setchar = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in setchar:
                setchar.remove(s[l])
                l += 1
            setchar.add(s[r])
            res = max(res, r - l + 1)
        return res