class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        #left and right pointers to show what part of array is in current "level"
        l, r = 0, 0

        while r < len(nums) - 1:
            #how far can the next level go 
            farthest = 0
            #set farthest variable equal to largest combo of jump distance and current index
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            #move pointers
            l = r + 1
            r = farthest
            #add one to res every iteration so you know how many "levels" there are
            res += 1
        return res


        