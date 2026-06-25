class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answerArr = []
        for i in range(len(nums)):
            p = 1
            lsit = nums.copy()
            del lsit[i]
            for num in lsit:
                p *= num
            answerArr.append(p)
        return answerArr

        