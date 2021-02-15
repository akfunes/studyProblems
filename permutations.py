# https://leetcode.com/problems/permutations/
class Solution:
    def __init__(self):
        self.numDict = {}
        self.permutations = []
        
    def recurse(self, i, j, nums):
        if i >= len(nums):
            return
        
        if j >= len(nums):
            return self.recurse(i+1, i+2, nums)
            
        # perform a swap between indices i and j
        n1 = nums[i]
        n2 = nums[j]
        tempNums = [x for x in nums]
        tempNums[i] = n2
        tempNums[j] = n1
            
        numString = ','.join(str(x) for x in tempNums)
        if numString not in self.numDict: 
            temp = [x for x in tempNums]
            self.permutations.append(temp)
            self.numDict[numString] = [x for x in tempNums]
            
        # use the swap
        self.recurse(i,j+1,tempNums)
        
        # don't use the swap
        self.recurse(i,j+1,nums)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        numString = ','.join(str(x) for x in nums)
        if numString not in self.numDict: 
            temp = [x for x in nums]
            self.permutations.append(temp)
            self.numDict[numString] = [x for x in nums]
            
        if len(nums) == 1:
            return self.permutations
        
        self.recurse(0,1,nums)
        return self.permutations

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        def backtrack(first):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
                
        ans = []
        n = len(nums)
        backtrack(0)
        return ans
        
