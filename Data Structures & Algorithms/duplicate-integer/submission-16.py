class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        l = defaultdict(list)
        for i in range(len(nums)):
            l[nums[i]]=l.get(nums[i], 0)+1

            if l[nums[i]]>1:
                return True
        return False
