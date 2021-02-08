# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        numWays = [1 for x in range(n+1)]
        
        for i in range(2,n+1):
            numWays[i] = numWays[i-1] + numWays[i-2]
        return numWays[n]
