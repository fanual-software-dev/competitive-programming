class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        citya = 0
        mincost = 0
        costs.sort(key = lambda x:x[0]-x[1])
        n = len(costs)//2

        for cost in costs:
            
            if citya!=n:
                mincost+=cost[0]
                citya+=1
            else:
                mincost+=cost[1]
        return mincost  
        