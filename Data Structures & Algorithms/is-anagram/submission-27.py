class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l = [0]*26
        for i in s:
            l[ord(i)-ord('a')]+=1
        for i in t:
            l[ord(i)-ord('a')]-=1
        return all(c==0 for c in l)
        
         
        

        
        

        
        





       
         

            
            