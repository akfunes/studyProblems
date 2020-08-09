# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def prependWord(self, currWord, reverseString):
        if currWord != "":
            if reverseString != "":
                reverseString = currWord + " " + reverseString
            else:
                reverseString = currWord
            currWord = ""

        return currWord, reverseString

    def reverseWords(self, s: str) -> str:
        currWord = ""
        reverseString = ""
        for c in s:
            if c == " ":
                currWord, reverseString = self.prependWord(currWord, reverseString)
            else:
                currWord += c

        currWord, reverseString = self.prependWord(currWord, reverseString)

        return reverseString
