# https://leetcode.com/problems/battleships-in-a-board/
class Solution:
    def __init__(self):
        self.visited = {}
        self.maxRows = 0
        self.maxCols = 0
        
    def findBounds(self, board, x, y):
        stack = []
        right = True 
        
        # either travel down or right in the matrix to find bounds of the ship
        if x + 1 < self.maxRows:
            if board[x+1][y] == "X":
                stack.append([x+1,y])
                right = False
        if y + 1 < self.maxCols:
            if board[x][y+1] == "X":
                stack.append([x,y+1])
            
        while len(stack) > 0:
            currIdx = stack.pop()
            currX = currIdx[0]
            currY = currIdx[1]
            if currX < self.maxRows and currY < self.maxCols:
                self.visited[str(currX) + "," + str(currY)] = 1
                if board[currX][currY] == "X":
                    board[currX][currY] = "."
                    if right:
                        stack.append([currX,currY+1])
                    else:
                        stack.append([currX+1,currY])
        return board
            
    def countBattleships(self, board: List[List[str]]) -> int:
        num = 0
        self.maxRows = len(board)
        self.maxCols = len(board[0])
        
        for x in range(self.maxRows):
            for y in range(self.maxCols):
                coordStr = str(x) + "," + str(y)
                if coordStr in self.visited:
                    continue
                else:
                    self.visited[coordStr] = 1
                    
                if board[x][y] =="X":
                    num += 1
                    board = self.findBounds(board, x, y)
                    
        return num
            
