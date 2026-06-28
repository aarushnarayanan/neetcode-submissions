class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0

        for r in range(len(s)):
            if s[r] in seen:
                left = max(seen[s[r]] + 1, left)
            seen[s[r]] = r
            res = max(res, r - left + 1)
        return res



        

            
            

        