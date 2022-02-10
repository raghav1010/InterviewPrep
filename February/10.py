#560. Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        dic = {}
        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur+=nums[i]
            if cur==k:
                ans+=1
            if dic.get(cur-k,0)>0:
                ans+=dic[cur-k]
            dic[cur]=dic.get(cur,0)+1
        return ans
            