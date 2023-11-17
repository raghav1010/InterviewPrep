class Solution:
    def minPairSum(self, nums):
        nums.sort()
        max_pair_sum = 0
        n = len(nums)
        for i in range(n):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n - 1 - i])
        return max_pair_sum
