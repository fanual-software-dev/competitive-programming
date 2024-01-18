class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seen = defaultdict(int)
        seen1 = defaultdict(int)
        for i in trips:
            seen[i[2]]+=i[0]
            seen1[i[1]]+=i[0]

        total = 0
        for i in range(1001):
            if i in seen1: total+=seen1[i]
            if i in seen: total-=seen[i]
            if total>capacity:
                return False
        return True
        
            
