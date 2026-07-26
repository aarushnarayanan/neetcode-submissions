class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            d = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [d, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        #at this point you now have the k closest points
        res = []
        #now pop all the values in the heap and append all points to res
        while maxHeap:
            d, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        
        return res




        