class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o={}
        for h in strs:
            key = ''.join(sorted(h))
            if key not in o:
                o[key]= []
            o[key].append(h)
        return list(o.values())

        
                    

            






                
        