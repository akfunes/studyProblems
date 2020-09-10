# https://leetcode.com/problems/prison-cells-after-n-days/
class Solution:
    def nextDay(self, cells):
        newCells = [0]*len(cells)
        for i in range(len(cells)):
            if i == 0:
                if cells[i] == 1:
                    newCells[i] = 0
            elif i == len(cells)-1:
                if cells[i] == 1:
                    newCells[i] = 0
            else:
                if cells[i-1] == cells[i+1]:
                    newCells[i] = 1
                else:
                    newCells[i] = 0

        return newCells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        stateDict = {}
        isFastForwarded = False

        while N > 0:
            if not isFastForwarded:
                stateKey = tuple(cells)
                if stateKey in stateDict:
                    N %= stateDict[stateKey] - N
                    isFastForwarded = True
                else:
                    stateDict[stateKey] = N
            if N > 0:
                N-=1
                nextCells = self.nextDay(cells)
                cells = nextCells


        return cells
