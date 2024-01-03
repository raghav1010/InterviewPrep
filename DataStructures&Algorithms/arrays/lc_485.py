class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_sum = 0
        max_one = 0
        for i in nums:
            if i == 0:
                max_one = max(max_one, one_sum)
                one_sum = 0
            else:
                one_sum += 1
        max_one = max(max_one, one_sum)
        return max_one
