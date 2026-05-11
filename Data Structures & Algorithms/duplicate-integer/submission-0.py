class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ok = {}

        for x in nums:
            ok[x] = ok.get(x,0)+1
        for i in ok:
            if ok[i]>1:
                return True
        return False
            