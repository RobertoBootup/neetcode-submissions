class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sort = sorted(nums)
        for i in range(len(nums) -1):
            if sort[i]==sort[i+1]:
                return True
        return False
        