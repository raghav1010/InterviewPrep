class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_map = [0] * (len(nums) + 1)
        for i in nums:
            hash_map[i] = 1

        for i in range(len(nums) + 1):
            if hash_map[i] == 0:
                return i
