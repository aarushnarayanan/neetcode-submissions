class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #keep running value as you iterate through triplet set
        max_triplet = (0, 0, 0)
        for a, b, c in triplets:
            maxA = max_triplet[0]
            maxB = max_triplet[1]
            maxC = max_triplet[2]
            #skip over unusable triplets
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            max_triplet = [max(maxA, a), max(maxB, b), max(maxC, c)]
            if max_triplet == target:
                return True
        return False


        
            




        

        
        