#532. K-diff Pairs in an Array
from collections import Counter
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int: 
        ans=0
        counter=Counter(nums)
        for x in counter:
            if k>0 and x+k in counter:
                ans+=1
            elif k==0 and counter[x]>1:
                ans+=1
        return ans