class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key = lambda x: x[0]**2 + x[1]**2)

        ans = [points[i] for i in range(k)]

        return ans