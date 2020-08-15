# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charDict = {}
        index = 0
        ans = []

        for c in S:
            charDict[c] = index
            index += 1

        i = 0
        while i < len(S):
            current = S[i]
            end = charDict[current]
            if end != i:
                j = i + 1

                while j != end:
                    nextChar = S[j]
                    if charDict[nextChar] > end:
                        end = charDict[nextChar]
                    j += 1
            ans.append(end-i+1)
            i = end + 1
        return ans
