# https://leetcode.com/problems/insert-delete-getrandom-o1/
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.setList = []
        self.setDict = {}
        self.length = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self.setDict:
            self.setDict[val] = self.length
            self.length += 1
            self.setList.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.setDict:
            # swap the value being deleted with the last element in the list
            # delete value from dictionary and list after swap
            # update dictionary with new index
            valIndex = self.setDict[val]
            self.setList[valIndex] = self.setList[self.length-1]
            self.setDict[self.setList[valIndex]] = valIndex
            self.setList.pop()
            del self.setDict[val]
            self.length -= 1
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        pickIndex = int(random.random() * self.length)
        return self.setList[pickIndex]
