from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)  # no cooldown needed

        # Step 1: Count tasks and create max-heap
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # stores pairs [remaining_count, ready_time]

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                # Step 2: Pop task with max frequency
                cnt = 1 + heapq.heappop(maxHeap)  # decrement count
                if cnt != 0:
                    # Step 3: Add to cooldown with ready time
                    cooldown.append([cnt, time + n])
            
            # Step 4: Release tasks from cooldown if their time is up
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time
