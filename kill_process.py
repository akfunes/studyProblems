# https://leetcode.com/problems/kill-process/
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = {}
        for i in range(len(pid)):
            parent = ppid[i]
            child = pid[i]
            if parent in graph:
                graph[parent].append(child)
            else:
                graph[parent] = [child]


        ans = []
        stack = []
        stack.append(kill)
        ans.append(kill)

        while stack:
            curr = stack.pop()
            if curr in graph:
                for item in graph[curr]:
                    stack.append(item)
                    ans.append(item)
        return ans
