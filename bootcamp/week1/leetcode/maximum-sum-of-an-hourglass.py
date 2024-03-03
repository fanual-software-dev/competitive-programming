class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        total = 0
        for row in range(len(grid)-2):
            for col in range(1,len(grid[0])-1):
                total = max(total,grid[row][col-1]+grid[row][col]+grid[row][col+1]+ grid[row+1][col]+ grid[row+2][col-1]+grid[row+2][col]+grid[row+2][col+1])
        return total            
        