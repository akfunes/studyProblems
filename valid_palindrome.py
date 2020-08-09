# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 2:
            if s[0].isalnum() and s[1].isalnum():
                return s[0].lower() == s[1].lower()
            else:
                if s[0].isalpha() or s[1].isalpha():
                    return True
        i = 0
        j = len(s)-1
        while i <= j:
            c1 = s[i]

            if not c1.isalnum():
                i+=1
                continue
            c2 = s[j]

            if not c2.isalnum():
                j-=1
                continue

            if c1.lower() != c2.lower():
                return False

            i+=1
            j-=1

        return True
