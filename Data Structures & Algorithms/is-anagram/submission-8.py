class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        asc=26*[0]
        a = 0
        for c in s:
            asc[ord(c)-ord('a')] +=1
        for c in t:
            asc[ord(c)-ord('a')]-=1
        return all(x==0 for x in asc)
            