#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
        
        m = prices[0]
        ans = 0
        for i in range(1,len(prices)):

            if(prices[i]<m):
                m = prices[i]
            else:
                ans = max(ans,prices[i]-m)
        return ans