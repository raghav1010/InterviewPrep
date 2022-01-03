#997. Find the Town Judge
class Solution:
    def findJudge(self, n, trust):
        if len(trust)<n-1:

            return -1 
        res =[0]*(n+1)
        for a,b in trust:
            res[a]-=1
            res[b]+=1
        for i in range(1,len(res)):
            if res[i]==n-1:
                return i
        return -1