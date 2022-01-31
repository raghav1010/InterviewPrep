#1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts):
        
        rows = len(accounts)
        columns = len(accounts[0])
        ans = -1
        for i in range(rows):
            ans = max(ans,sum(accounts[i]))
        
        return ans