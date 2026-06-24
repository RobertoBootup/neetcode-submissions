class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uno = [0]*26
        dos = [0]*26
        
        for i in s:
            uno[(ord(i)-ord('a'))]+=1
        for i in t:
            dos[(ord(i)-ord('a'))]-=1
        return all(i + j == 0 for i, j in zip(uno, dos))
        


         
        

        
        

        
        





       
         

            
            