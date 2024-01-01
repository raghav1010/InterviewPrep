class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        peak_ele_count = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                peak_ele_count += 1
        if nums[-1] > nums[0]:
            peak_ele_count += 1
        return peak_ele_count <= 1
