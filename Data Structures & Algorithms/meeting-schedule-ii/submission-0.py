"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        data = []

        for i in intervals:
            s = i.start
            e = i.end
            data.append((s, +1))
            data.append((e, -1))
        
        data.sort()

        cur = 0
        ans = 0
        for _, v in data:
            cur += v
            ans = max(ans, cur)
        return ans
        