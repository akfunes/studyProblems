class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # edge cases
        if len(words) == 2 and words[0] == words[1]:
            return words[0]

        graph = {}
        # generate graph
        for w in words:
            for c in w:
                if c not in graph:
                    graph[c] = []

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(min(len(w1),len(w2))):
                c1 = w1[j]
                c2 = w2[j]

                if c1 != c2:
                    if c1 not in graph:
                        graph[c1] = [c2]
                    else:
                        if c2 not in graph[c1]:
                            graph[c1].append(c2)
                    break

        # generate list of incoming edges
        inDegrees = {}
        for key in graph:
            if key not in inDegrees:
                inDegrees[key] = 0

            for c in graph[key]:
                if c in inDegrees:
                    inDegrees[c] += 1
                else:
                    inDegrees[c] = 1

        L = ""
        S = []
        # fill S with nodes with no incoming edges
        for k, v in inDegrees.items():
            if v == 0:
                S.append(k)

        # top sort
        while S:
            n = S.pop(0)
            L += n
            if n in graph:
                for m in graph[n]:
                    # "remove edge" by decrementing inDegrees
                    inDegrees[m] -= 1
                    if inDegrees[m] == 0:
                        S.append(m)

        # if edge still in graph then a cycle exists
        for v in inDegrees.values():
            if v > 0:
                return ""
        return L
