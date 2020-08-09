class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)

        if sLen == 0:
            return ""
        elif sLen == 1:
            return s
        else:
            longest = 0
            res = ""
            for i in range(len(s)-1):
                # find a palindrome that expands outward
                findResult = self.findLongestPalindrome(s,i,i,0)
                findResult2 = self.findLongestPalindrome(s,i,i+1,0)
                findMax = max(findResult, findResult2)
                if findMax > longest:
                    longest = findMax
                    start = i - (findMax-1) // 2
                    end = i + findMax // 2
                    res = s[start:end+1]
        return res

    def findLongestPalindrome(self, s, left, right, currLen):
        if (left < 0 or right >= len(s)):
            return currLen

        leftChar = s[left]
        rightChar = s[right]

        if left == right:
            currLen += 1
        elif leftChar == rightChar:
            currLen += 2
        else:
            return currLen

        return(self.findLongestPalindrome(s, left-1, right+1, currLen))
