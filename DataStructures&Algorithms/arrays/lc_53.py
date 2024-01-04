class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pos = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                pos = i
                break
        if pos == -1:
            return max(nums)

        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            if sum1 + nums[i] > 0:
                sum1 = sum1 + nums[i]
                sum2 = max(sum2, sum1)
            else:
                sum1 = 0

        return sum2

#         pos =-1
#         for i in range(len(nums)):
#             if (nums[i]>0):
#                 pos = i
#                 break
#         if pos ==-1:
#             return max(nums)

#         sum1 = 0
#         sum2 = 0
#         for i in range(len(nums)):
#             if (sum1+nums[i]>0):
#                 sum1 = sum1+nums[i]
#                 sum2 = max(sum1,sum2)
#             else:

#                 sum1 = 0

#         return max(sum2,sum1)
