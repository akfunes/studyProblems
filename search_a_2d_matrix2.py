# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def binSearch(self,matrix, start, target, isVert):
        lo = start
        if isVert:
            hi = len(matrix[0])
        else:
            hi = len(matrix)
        hi -= 1

        while lo <= hi:
            mid = (hi+lo)//2
            if isVert:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False


        for i in range(min(len(matrix[0]),len(matrix))):
            inVert = self.binSearch(matrix,i,target,True)
            inHoriz = self.binSearch(matrix,i,target,False)

            if inVert or inHoriz:
                return True

        return False
