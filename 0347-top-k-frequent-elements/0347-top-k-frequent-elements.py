class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         random=Counter(nums)
         ans=dict(sorted(random.items(),key=lambda x:x[1],reverse=True))
         res=[]
         for i in ans.keys():
             res.append(i)
         return res[:k]
        