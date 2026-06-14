class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_index = len(nums) // 2
        mid_int = nums[mid_index]
        if target > mid_int:
            for i in range(mid_index, len(nums)):
                if nums[i] == target:
                    return i
        elif target < mid_int:
            for i in range(mid_index):
                if nums[i] == target:
                    return i
        else: 
            return mid_index
        return -1
        