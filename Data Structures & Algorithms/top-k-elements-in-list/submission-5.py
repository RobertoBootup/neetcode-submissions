class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        a = []

        for i in nums:
            h[i]=h.get(i,0)+1
            
        for j in range(k):
            q = max(h, key=h.get)
            a.append(q)
            h[q]=0
        return (a)


           

        