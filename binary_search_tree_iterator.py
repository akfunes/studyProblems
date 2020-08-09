# https://leetcode.com/problems/binary-search-tree-iterator/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        i = 0
        for c in order:
            orderDict[c] = i
            i +=1

        for i in range(len(words)-1):
            found = False
            for j in range(min(len(words[i]),len(words[i+1]))):
                c1 = words[i][j]
                c2 = words[i+1][j]

                if(c1 != c2):
                    if(orderDict[c1] > orderDict[c2]):
                        return False
                    found = True
                    break
            if not found and len(words[i]) > len(words[i+1]):
                return False
        return True
