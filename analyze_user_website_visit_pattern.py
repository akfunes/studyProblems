# https://leetcode.com/problems/analyze-user-website-visit-pattern/
import heapq
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        users = defaultdict(list)
        heap = []

        # sort visits by time and create a dictionary of sites visited by user
        for i in range(len(username)):
            heapq.heappush(heap,(timestamp[i], website[i], username[i]))

        while heap:
            time, site, user = heapq.heappop(heap)
            users[user].append(site)


        # generate the 3 sequence permutations and track repeat sequences in dictionary
        count = defaultdict(int)
        maximum = 0
        res = tuple()

        for key,value in users.items():
            combos = combinations(value, 3)

            # remove duplicates from the permutations and iterate
            for combo in set(combos):
                count[combo] += 1

                if count[combo] > maximum:
                    maximum = count[combo]
                    res = combo
                elif count[combo] == maximum:
                    if combo < res:
                        res = combo

        return list(res)
