class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_moves = 0
        while maxDoubles>0 and target>1:
            min_moves+=1+target%2
            maxDoubles-=1
            target = target//2
        return min_moves+target-1
        
        