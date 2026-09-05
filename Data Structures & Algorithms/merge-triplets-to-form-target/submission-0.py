class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplet_set = set()

        #form set of all usable triples
        for a, b, c in triplets:
            #only include triplets where all values are less than target values
            #if any value in a triplet is greater than its corresponding target value that triplet will never form target no matter what other triplet you compare it to
            if a <= target[0] and b <= target[1] and c <= target[2]:
                triplet_set.add((a, b, c))

        #keep running value as you iterate through triplet set
        max_triplet = (0, 0, 0)
        for a, b, c in triplet_set:
            maxA = max_triplet[0]
            maxB = max_triplet[1]
            maxC = max_triplet[2]
            max_triplet = (max(maxA, a), max(maxB, b), max(maxC, c))
            if list(max_triplet) == target:
                return True
        return False


        
            




        

        
        