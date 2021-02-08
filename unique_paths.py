# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        d = [[1 for y in range(n)] for x in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i][j-1] + d[i-1][j]
        return d[m-1][n-1]
