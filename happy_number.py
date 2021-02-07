# https://leetcode.com/problems/happy-number/
class Solution:
    def findSum(self,n):
        s = 0
        while n > 0:
            digit = n%10
            if digit > 0:
                s += digit ** 2
            n = n//10
        return s
            
    def isHappy(self, n: int) -> bool:
        
        sumSet = set()
        currSum = self.findSum(n)
        
        while  currSum != 1:
            sumSet.add(currSum)
            currSum = self.findSum(currSum)
            
            if currSum in sumSet:
                return False
            else:
                sumSet.add(currSum)
        return True

