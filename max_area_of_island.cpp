// https://leetcode.com/problems/max-area-of-island/
#include <tuple>
class Solution {
public:
    int maxRows = 0;
    int maxCols = 0;
    
    int getIslandBounds(vector<vector<int>>& grid, int i, int j){
        vector<std::tuple<int,int>> stack;
        stack.push_back(std::make_tuple(i,j));
        int area = 0;
        
        while(stack.size() > 0){
            std::tuple<int,int> currItem = stack.back();
            stack.pop_back();
            i = std::get<0>(currItem);
            j = std::get<1>(currItem);
            
            
            // Find bounds of island
            if (grid[i][j] == 1){
                area++;
                grid[i][j] = 0;
                // Attempt to travel north, south, west, or east
                if (i-1 >= 0)
                    stack.push_back(std::make_tuple(i-1,j));
                if (i+1 < maxRows)
                    stack.push_back(std::make_tuple(i+1,j));
                if (j-1 >= 0)
                    stack.push_back(std::make_tuple(i,j-1));
                if (j+1 < maxCols)
                    stack.push_back(std::make_tuple(i,j+1));
            }
            
        }
        return area;
    }
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        maxRows = grid.size();
        maxCols = grid[0].size();
        
        for (int i = 0; i < maxRows; i++){
            for (int j = 0; j < maxCols; j++){
                if (grid[i][j] == 1){
                    maxArea = std::max(maxArea,getIslandBounds(grid,i,j));
                }
            }
        }
        return maxArea;
    }
};
