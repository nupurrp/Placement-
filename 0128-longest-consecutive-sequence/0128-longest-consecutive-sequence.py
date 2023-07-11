class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for val in nums:
            if val in s:
                currSize = 1
                temp1,temp2 = val,val

                while temp1 + 1 in s:
                    currSize += 1
                    s.remove(temp1 + 1)
                    temp1 += 1

                while temp2 - 1 in s:
                    currSize += 1
                    s.remove(temp2 - 1)
                    temp2 -= 1

                s.remove(val)
                res = max(res,currSize)

        return res
        