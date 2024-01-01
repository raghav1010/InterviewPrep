class Solution:

    def reverse(self, nums, i, j):
        li = i
        lj = j
        while li < lj:
            temp = nums[li]
            nums[li] = nums[lj]
            nums[lj] = temp
            li += 1
            lj -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
