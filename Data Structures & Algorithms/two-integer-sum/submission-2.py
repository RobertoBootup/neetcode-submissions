class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for c in nums:
            
            targ = target -c
            if targ in seen:
                return[seen[targ],len(seen)]
            seen[c] = len(seen)