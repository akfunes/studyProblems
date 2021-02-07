# https://leetcode.com/problems/decode-ways/
from collections import defaultdict
class Solution:
    def __init__(self):
        self.numDecode = 0
        self.s = None
        
    @lru_cache(maxsize=None)    
    def recurse(self, i, s):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i == len(s)-1:
            return 1
        
        answer = self.recurse(i+1, s)
        if int(s[i:i+2]) <= 26:
            answer += self.recurse(i+2, s)
        return answer
        
        
            
    def numDecodings(self, s: str) -> int:
        return self.recurse(0,s)

