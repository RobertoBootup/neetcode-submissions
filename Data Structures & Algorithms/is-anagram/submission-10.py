class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m ={}
        for c in s:
            m[c] = m.get(c,0)+1
        for c in t:
            m[c] = m.get(c,0)-1
        return all (v==0 for v in m.values())
        

            