class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        max_time = 0

        processorTime.sort()
        tasks.sort()

        for i in range(4,len(tasks)+1,4):

            max_time = max(max_time,tasks[i-1]+processorTime.pop())
        return max_time

        