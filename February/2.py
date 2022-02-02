#438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashp = [0]*(26)
        hashs = [0]*(26)
        if len(s)<len(p):
            return []
        
        for i in range(len(p)):
            hashp[ord(p[i])-ord('a')]+=1
        
        output = []
        n=len(s)
        m=len(p)
        
        for i in range(n):
            hashs[ord(s[i])-ord('a')]+=1
            
            if i>=m:
                hashs[ord(s[i-m])-ord('a')]-=1
            
            if hashp==hashs:
                output.append(i-m+1)
        
        return output
    