class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)

        for i in range(k):
            kth = heapq.heappop(nums)
            if i == k - 1:
                return (kth * - 1)
        