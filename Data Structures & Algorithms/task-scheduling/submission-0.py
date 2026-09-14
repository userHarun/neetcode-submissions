import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freq = [0] * 26
        for task in tasks:
            asci = ord(task) - ord('A')
            freq[asci] += 1
        heap = []
        for fr in freq:
            if fr > 0:
                heapq.heappush(heap, fr * -1)
        q = deque() # holds pairs: (remaining_tasks, ready_again_at)
        while q or heap:
            time += 1
            if heap:
                # get remaining tasks
                remaining_tasks = (-1 * heapq.heappop(heap)) - 1
                # if there are more tasks append to queue
                if remaining_tasks > 0:
                    q.append([remaining_tasks, time + n])



                
            # if its ready to be used again
            if q and q[0][1] == time:
                # append to remaining tasks to heap
                heapq.heappush(heap, -1 * q.popleft()[0])



        return time

'''

the task that should be processed first is the one with the largest freq
use heap to retreive the maximum element from our freq after a cooldown

'''