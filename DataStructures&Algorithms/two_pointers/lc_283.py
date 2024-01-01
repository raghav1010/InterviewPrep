class Solution:
    def swap(self, nums, i, j):
        li = i
        lj = j
        temp = nums[li]
        nums[li] = nums[lj]
        nums[lj] = temp

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                self.swap(nums, i, j)
                i = i + 1
