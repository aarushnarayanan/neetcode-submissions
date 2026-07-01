class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #take out case where t empty
        if t == "":
            return ""
        
        count, window = {}, {}
        #setting up t
        for char in t:
            count[char] = 1 + count.get(char, 0)

        #distinct chars we have vs distinct chars we need
        have, need = 0, len(count)
        res = [-1, -1]
        res_len = float("infinity")
        l = 0

        #sliding window
        for r in range(len(s)):
            #keep going right til all chars in substring are found
            c = s[r]
            window[c] = 1 + window.get(c, 0) 
            if c in count and window[c] == count[c]:
                have += 1
            #shrink from left while window valid
            while have == need:
                #update result if window smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                #remove left char from window
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if res_len != float("infinity") else ""


            
            






        
        

        

        

            


            
        