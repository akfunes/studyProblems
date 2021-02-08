# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxRows = len(grid)-1
        maxCols = len(grid[0])-1
        
        for i in range(maxRows, -1, -1):
            for j in range(maxCols, -1,-1): 
                # current coords is bottom row, disregard last index
                if i == maxRows and j < maxCols:
                    grid[i][j] = grid[i][j+1] + grid[i][j]
                # current coords is middle rows and not last column
                elif i < maxRows and j < maxCols:
                    grid[i][j] = min(grid[i+1][j],grid[i][j+1]) + grid[i][j]
                # current coords is middle rows and last column
                elif i < maxRows and j == maxCols:
                    grid[i][j] = grid[i+1][j] + grid[i][j]
                    
        return grid[0][0]
