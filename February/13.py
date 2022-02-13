#78. Subsets
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        output=[[]]
        for num in nums:
            output=output+[curr+[num]for curr in output]
        return output