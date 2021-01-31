# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        EAST = 0
        SOUTH = 1
        WEST = 2
        NORTH = 3
        # used to update the current coordinate based on direction being travelled
        # [east,south,west,north]
        COORD_UPDATE = [[0,1],[1,0],[0,-1],[-1,0]]  
        northBoundary = westBoundary = 0
        eastBoundary = len(matrix[0])-1
        southBoundary = len(matrix)-1
        
        currentDir  = EAST # always start traveling east
        currentLoc = [1,0]
        ans = []
        
        for i in range(len(matrix)*len(matrix[0])):
            val = matrix[currentLoc[0]][currentLoc[1]]
            ans.append(val)
            
            if currentDir == EAST and currentLoc[1] >= eastBoundary:
                currentDir = SOUTH
                northBoundary += 1
            elif currentDir == SOUTH and currentLoc[0] >= southBoundary:
                currentDir = WEST
                eastBoundary -= 1
            elif currentDir == WEST and currentLoc[1] <= westBoundary:
                currentDir = NORTH
                southBoundary -= 1
            elif currentDir == NORTH and currentLoc[0] <= northBoundary:
                currentDir = EAST
                westBoundary += 1
                
            currentLoc[0] += COORD_UPDATE[currentDir][0]
            currentLoc[1] += COORD_UPDATE[currentDir][1]
            
        return ans
