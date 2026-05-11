class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref1 = [0]*26
        ref2 = [0]*26
        for char in s:
            index = ord(char)-ord('a')
            ref1[index] +=1
        for char in t:
            index1 = ord(char)-ord('a')
            ref2[index1]+=1
        if ref1 == ref2:
            return True
        else:
            return False


        
        