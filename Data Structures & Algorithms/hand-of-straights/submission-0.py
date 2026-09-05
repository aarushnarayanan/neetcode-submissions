class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for num in hand:
            start = num
            #keep walking along count to find the lowest possible start index
            while count[start - 1]:
                start -= 1
            #walks back up chain from start to num
            while start <= num:
                #if there's a copy of the value being looked for keep going, while loop because there can be multiple groups with the same value in them
                while count[start]:
                    #from starting point go til the numbers in groupSize and if any of them aren't in the dictionary count then return False
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        #subtract one from the count 
                        count[i] -= 1
                #add one to starting number so next group can be formed
                start += 1
        return True
            
            
        

            
        
        
        

        