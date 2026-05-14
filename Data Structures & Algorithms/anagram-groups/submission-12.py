class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for word in strs:
            ray =[0]*26
            
            for i in word:
                ind = ord(i)-ord('a')
                ray[ind]+=1
            ok = tuple(ray)
            if ok not in h:
                h[ok]=[]
            h[ok].append(word)

        return list(h.values())
                





        