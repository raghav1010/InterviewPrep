#525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        ans = 0
        hashmap ={}
        count = 0
        for i in range(len(nums)):
            cur = nums[i]
            if (cur==0):
                count-=1
            else:
                count+=1
            
            if count ==0:
                ans= i+1 
                
            if hashmap.get(count,-1)!=-1:
                ans= max(ans,i-hashmap[count])
            else:
                hashmap[count]=i
        return ans