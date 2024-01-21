class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, stop: int) -> int:

        ans1 = 0
        ans2 = 0
       
        for i in range(min(start,stop),max(start,stop)):
            ans1+=distance[i]
        for i in range(max(start,stop),len(distance)+min(start,stop)):
            ans2+=distance[i%len(distance)]
        return min(ans1,ans2)



        