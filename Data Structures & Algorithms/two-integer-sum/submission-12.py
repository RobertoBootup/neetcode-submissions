class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            
            if answer in h:
                
                return[h[answer],i]
            h[nums[i]]= i
                
        
        





        