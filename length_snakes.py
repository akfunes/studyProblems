def findLengthSnakes(matrix):
    # Depth first search: recurse until end of the snake is found (adjacent indices are all zeroes)
    def dfs(row, col):
        # Base case: Return if current index is not part of the snake or visit the
        #            current index by setting value to zero so that we don't double count a snake
        if matrix[row][col] == 0:
            return 0
        else:
            matrix[row][col] = 0

        # Visit adjacent nodes if it is within the bounds of the matrix.
        # Do not count nodes that are diagonal of the current location.
        # Always attempt to visit each adjacent node in case the snake
        # is not straight such as an "s" shape.
        north = south = west = east = 0
        if row - 1 > 0:
            north = dfs(row-1, col)
        if row + 1 < len(matrix):
            south = dfs(row+1, col)
        if col - 1 > 0:
            west = dfs(row, col-1)
        if col + 1 < len(matrix[0]):
            east = dfs(row, col+1)

        # Sum the results in order to generate the total length of the snake
        return north + south + west + east + 1

    # Initialize list to store the answer
    result = []

    # Iterate through each node to find the start of a snake
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            current = matrix [row][col]

            # Call depth first search if the current node is a piece of a snake
            if current == 1:
                result.append(dfs(row,col))
    return result

def main():
    # Square matrix
    matrix1 = [
    		[1, 0, 0, 1, 0],
    		[1, 0, 1, 0, 0],
    		[0, 0, 1, 0, 1],
    		[1, 0, 1, 0, 1],
    		[1, 0, 1, 1, 0],
    		]

    # Rectangle matrix: Rows > Cols
    matrix2 = [
    		[1, 0, 0, 1, 0],
    		[1, 0, 1, 0, 0],
    		[0, 0, 1, 0, 1],
    		[1, 0, 1, 0, 1],
    		[1, 0, 1, 1, 0],
    		[1, 0, 0, 0, 0],
    		]

    # Rectangle matrix: Cols > Rows
    matrix3 = [
    		[1, 0, 0, 1, 0, 0],
    		[1, 0, 1, 0, 0, 0],
    		[0, 0, 1, 0, 1, 0],
    		[1, 0, 1, 0, 0, 0],
    		[1, 0, 1, 1, 0, 0],
    		]

    # Rectangle matrix: Cols > Rows
    matrix4 = [
    		[1, 0, 0, 1, 0, 0],
                ]

    print("Case 1:")
    print(findLengthSnakes(matrix1))
    print("Case 2:")
    print(findLengthSnakes(matrix2))
    print("Case 3:")
    print(findLengthSnakes(matrix3))
    print("Case 4:")
    print(findLengthSnakes(matrix4))

main()
