class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            targ = target-nums[i]
            if targ in mapp:
                return [mapp[targ],i]
            mapp[nums[i]] = i