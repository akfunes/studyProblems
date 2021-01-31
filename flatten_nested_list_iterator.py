# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.loadNestedList(0, nestedList)
        
    def loadNestedList(self,index, nestedList) :
        if index >= len(nestedList):
            return
        
        self.loadNestedList(index+1,nestedList) # traverse to furthest depth of the nested list first
        if nestedList[index].isInteger(): # retrieve data from each neted list
            self.stack.append(nestedList[index].getInteger())
        else:
            self.loadNestedList(0,nestedList[index].getList())
        
    def next(self) -> int:
        return self.stack.pop()
        
    
    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        else:
            return False
                
                
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
