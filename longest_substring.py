class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1):
            return len(s)

        charDict = {}
        ans = 0
        x = 0

        for y in range(0,len(s)):
            c = s[y]
            if c in charDict:
                if (charDict[c] > x):
                    x = charDict[c]

            if y-x+1 > ans:
                ans = y-x+1
            charDict[c] = y + 1
            y +=1

        return ans
