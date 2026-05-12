class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m ={}
        for x in nums:
            m[x] = m.get(x,0)+1
            if m[x]>1:
                return True
        return False
        
        