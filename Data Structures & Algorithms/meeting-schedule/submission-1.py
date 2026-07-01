"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
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
        
        return True if ans == 1 else False
