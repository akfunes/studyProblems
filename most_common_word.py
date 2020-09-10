# https://leetcode.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        seen = {}
        bannedDict = {}
        top = ["",0]

        for word in banned:
            bannedDict[word.lower()] = 1

        currentWord = ""
        for c in paragraph:
            if c.isalpha():
                currentWord += c.lower()
            else:
                if currentWord != "":
                    if currentWord not in bannedDict:
                        if currentWord in seen:
                            seen[currentWord] += 1
                        else:
                            seen[currentWord] = 1

                        if top[1] < seen[currentWord]:
                            top[0] = currentWord
                            top[1] = seen[currentWord]

                    currentWord = ""


        if currentWord != "":
            if currentWord not in banned:
                if currentWord in seen:
                    seen[currentWord] += 1
                else:
                    seen[currentWord] = 1

                if top[1] < seen[currentWord]:
                    top[0] = currentWord
                    top[1] = seen[currentWord]

        return top[0]
