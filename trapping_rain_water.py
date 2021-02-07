# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        ans = 0
        size = len(height)
        leftMax = [ 0 for x in range(len(height))]
        rightMax = [ 0 for x in range(len(height))]
        leftMax[0] = height[0]
        rightMax[size-1] = height[size-1]
        
        for i in range(1,size):
            leftMax[i] = max(height[i],leftMax[i-1])
        
        for i in range(size-2,0,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
        
        for i in range(1,size):
            ans += min(leftMax[i],rightMax[i]) - height[i]
        
        return ans
