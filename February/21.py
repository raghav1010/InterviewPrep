#169. Majority Element
import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        return max(count.keys(),key=count.get)