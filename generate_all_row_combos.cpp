#include <vector>
#include <iostream>
#include <algorithm>

void generateCombos(std::vector<std::vector<int>> inMatrix, std::vector<std::vector<int>> refMatrix)
{
    if(refMatrix.size() == 0)
    {
        std::cout << "Matrix Combo: " << std::endl;
        for (auto& i : inMatrix) {
            for(auto& j : i) {
                std::cout << j;
            }
            std::cout << std::endl;
        }
        return;
    }

    inMatrix.push_back(refMatrix.front());
    refMatrix.erase(refMatrix.begin());

    // don't swap
    generateCombos(inMatrix, refMatrix);

    // do swap
    if(refMatrix.size() > 0)
    {
        inMatrix.back().swap(refMatrix.front());
        generateCombos(inMatrix, refMatrix);
    }
}

int main()
{
    std::vector<std::vector<int>> test = {{1,2,3}, {4,5,6}, {7,8,9}};
    std::vector<std::vector<int>> result;
    generateCombos(result, test);
    std::cout << std::endl;
    for (auto& i : result) {
        for(auto& j : i) {
            std::cout << j;
        }
        std::cout << std::endl;
    }
}
