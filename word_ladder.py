# https://leetcode.com/problems/word-ladder/
import queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        comboDict = {}

        for word in wordList:
            for i in range(len(word)):
                newWord = word[:i] + "*" + word[i+1:]
                if newWord in comboDict:
                    comboDict[newWord].append(word)
                else:
                    comboDict[newWord] = [word]

        visited = {}
        q = queue.Queue()
        q.put([beginWord,1])

        while not q.empty():
            currentItem = q.get()
            currentWord = currentItem[0]
            currentDepth = currentItem[1]

            for i in range(len(currentWord)):
                newWord = currentWord[:i] + "*" + currentWord[i+1:]

                if newWord in comboDict:
                    for word in comboDict[newWord]:
                        if word == endWord:
                            return currentDepth + 1

                        if word not in visited:
                            q.put([word, currentDepth+1])
                            visited[word] = 1

        return 0
