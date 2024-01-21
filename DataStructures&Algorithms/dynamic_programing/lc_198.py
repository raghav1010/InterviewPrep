class Solution:
    def rob(self, nums: List[int]) -> int:

        ans = 0
        t = [-1] * (len(nums) + 1)

        def solve(n):

            if n == 0:
                return 0

            if n == 1:
                return nums[n - 1]

            if t[n] != -1:
                return t[n]

            ans = max(solve(n - 1), solve(n - 2) + nums[n - 1])
            t[n] = ans
            return ans

        return solve(len(nums))
