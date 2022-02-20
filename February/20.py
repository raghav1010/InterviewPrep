#1288. Remove Covered Intervals
class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans = 0
        prev = 0
        for _,end in intervals:
            if end>prev:
                ans = ans+1
                prev = end
        return ans