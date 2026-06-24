class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            tarr = target - nums[i]
            if tarr in h:
                return [h[tarr],i]
            h[nums[i]] = i

                
        
        





        