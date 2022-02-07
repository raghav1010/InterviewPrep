#389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap=dict()
        for i in range(len(s)):
            hashmap[s[i]]= hashmap.get(s[i],0)+1
        print(hashmap)
        for j in range(len(t)):
            print(hashmap.get(t[j]))
            if hashmap.get(t[j],-1)==-1 or hashmap.get(t[j])==0:
                return t[j]
            else:
                hashmap[t[j]]-=1