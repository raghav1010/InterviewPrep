#1010 Pairs of Songs With Total Durations Divisible by 60
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        mapp = [0] * 60
        result = 0
        for x in time:
            result += mapp[-x % 60]
            mapp[x % 60] += 1
        return result