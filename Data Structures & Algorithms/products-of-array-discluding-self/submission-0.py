from math import prod
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            h = nums.copy()
            del h[i]
            y = prod(h)
            l.append(y)
        return(l)
