class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]< nums[i+1]:
                index = i
                break
        if index == -1:
            nums[:]=nums[::-1]
            return nums
        for i in range(n-1,index-1,-1):
            if nums[index]<nums[i]:
                nums[index],nums[i]=nums[i],nums[index]
                break
        nums[::]=nums[:index+1]+sorted(nums[index+1:])
        return nums


