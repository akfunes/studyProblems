# https://leetcode.com/problems/reorder-data-in-log-files/
import re
import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digIds = []
        letIds = []

        for log in logs:
            temp = log.split(" ")
            if(not len(temp)  > 1):
                continue

            if re.search("\d",temp[1]):
                digIds.append(log)
            else:
                key = log[log.find(" ") +1:] + " " + log[:log.find(" ")]
                key = key.split()
                letIds.append([key,log])

        list.sort(letIds, key=lambda ident: ident[0])
        ans = [x[1] for x in letIds]
        for ident in digIds:
            ans.append(ident)

        return ans
