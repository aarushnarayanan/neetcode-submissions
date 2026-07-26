class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #turn nums into a minHeap
        heapq.heapify(nums)
        
        while len(nums) != k:
            heapq.heappop(nums)

        return nums[0]

        