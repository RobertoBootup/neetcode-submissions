class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dich = defaultdict(list)
        for word in strs:
            chey = [0]*26
            for i in word:
                chey[ord('a')-ord(i)]+=1
            o = tuple(chey)
            dich[o].append(word)
        return list(dich.values())
            
                
                
        
        



        