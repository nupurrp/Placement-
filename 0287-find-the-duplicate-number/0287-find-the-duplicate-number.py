class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=Counter(nums)
        return nums.most_common()[0][0]
        