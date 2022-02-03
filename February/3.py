#454. 4Sum II
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        ans = 0
        hashmap={}
        for a in nums1:
            for b in nums2:
                hashmap[a+b]=hashmap.get(a+b,0)+1
        
        for c in nums3:
            for d in nums4:
                ans = ans+hashmap.get(-(c+d),0)
        return ans