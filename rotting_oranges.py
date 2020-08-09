import queue
class Solution:
    def inBounds(self,grid, r, c):
        if r >= 0 and r < len(grid):
            if c >= 0 and c < len(grid[0]):
                return True

        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = 0
        q = queue.SimpleQueue()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten += 1
                    q.put([r,c,0])
        numDay = 0
        while not q.empty():
            item = q.get()
            print(item)
            r = item[0]
            c = item[1]
            day = item[2]

            if day > numDay:
                numDay = day

            if self.inBounds(grid, r-1, c):
                if grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.put([r-1,c,day+1])
            if self.inBounds(grid, r+1, c):
                if grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.put([r+1,c,day+1])
            if self.inBounds(grid, r, c-1):
                if grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.put([r,c-1,day+1])
            if self.inBounds(grid, r, c+1):
                if grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.put([r,c+1,day+1])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return numDay
