class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #immedeately check if s2 is less than s1
        if len(s2) < len(s1):
            return False
        #create alphabetic char count arrays for s1 and s2
        s1Count = [0] * 26
        s2Count = [0] * 26


        #modify char count arrays for both strings 
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        #initialize how much of the two strings match together
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        #fixed sliding window size of s1
        l = 0
        for r in range(len(s1), len(s2)):
            # if at any point all string matches are equal then return True
            if matches == 26:
                return True
            #setting index to the chars corresponding point
            index = ord(s2[r]) - ord('a')
            #increase count of char by 1
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


        
        