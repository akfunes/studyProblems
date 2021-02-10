# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def findEndLeadingSpaces(self,s):
        spaceIndex = 0
        for c in s:
            if c == " ":
                spaceIndex += 1
            else:
                return spaceIndex
        return spaceIndex
    
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0 
        
        endLeadingSpace = self.findEndLeadingSpaces(s)
        loBound = -2**31
        hiBound = 2**31 -1
        sign = 1
        num = 0
        
        if endLeadingSpace < len(s):
            if s[endLeadingSpace] == "-":
                sign = -1
                endLeadingSpace += 1
            elif s[endLeadingSpace] == "+":
                endLeadingSpace += 1
            
        for c in s[endLeadingSpace:]:
            if c.isdigit():
                num = num * 10
                num += int(c)
            else:
                break
        
        # assign sign by multiplying by -1/1
        num = num * sign
        
        # clamp down result if it cannot be stored in 32 bits
        if sign == 1 and num > hiBound:
            return hiBound
        if sign == -1 and num < loBound:
            return loBound
            
        return num
