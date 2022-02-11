#567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        hash_val = [0]*26
        
        for s1_val in s1:
            hash_val[ord(s1_val)-ord('a')] +=1
        
        for i in range(len(s1)):
            hash_val[ord(s2[i])-ord('a')] -=1
        
        if hash_val == [0]*26:
            return True
        
        k = len(s1)
        
        for i in range(k,len(s2)):
            hash_val[ord(s2[i-k])-ord('a')] +=1
            hash_val[ord(s2[i])-ord('a')] -=1
            if hash_val == [0]*26:
                return True
            
        return False  