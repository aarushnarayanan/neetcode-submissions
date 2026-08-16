class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create a frequency counter of all letters in tasks
        count = Counter(tasks)
        #the frequency counter into a maxHeap
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        #use time to see how long to wait between tasks
        time = 0
        #use a queue to see whats in cooldown
        q = deque()
        #while there's tasks left to do or tasks in cooldown
        while maxHeap or q:
            time += 1
            #if theres nothing in the heap skip the time to the cooldown time in queue
            if not maxHeap:
                time = q[0][1]
            else:
                #decrease the count of the task by 1
                c = 1 + heapq.heappop(maxHeap)
                #if there's more tasks for a letter left append that letter to the cooldown queue with the time that task can start back up at
                if c:
                    q.append([c, time + n])
            #if the cooldown queue has elements left and the current time is equal to the time in the cooldown queue push that task back into the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                
        
        
        