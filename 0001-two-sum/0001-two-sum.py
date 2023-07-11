class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            for j,z in enumerate(nums):
                t = v + z
                if t == target and i!=j:
                    return i,j