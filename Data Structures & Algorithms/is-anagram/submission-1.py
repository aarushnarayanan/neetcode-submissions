class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq_map = {}
        t_freq_map = {}
        for s_char in s:
            if s_char in s_freq_map:
                s_freq_map[s_char] += 1
            else:
                s_freq_map[s_char] = 1
        for t_char in t:
            if t_char in t_freq_map:
                t_freq_map[t_char] += 1
            else:
                t_freq_map[t_char] = 1
        for s_freq_char in s_freq_map:
            if s_freq_map[s_freq_char] != t_freq_map.get(s_freq_char, 0):
                return False
        return True