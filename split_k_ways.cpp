#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<vector<vector<int>>> subsets;
int K;

void printSubSet(vector<vector<int>> tempVec)
{
    int i = 0;
    auto currVecIndex = tempVec.begin();
    auto currVec = currVecIndex->begin();
    while(currVecIndex != tempVec.end())
    {
        cout << "Subset: " << i << endl;
        i++;
        for(auto it = currVec; it != currVecIndex->end(); ++it)
        {
            cout << *it << endl;
        }
        cout << "-----" << endl;
        ++currVecIndex;
        currVec = currVecIndex->begin();
    }
}

void shiftElements(vector<vector<int>>& vec, int subSetIndex)
{
    if(vec[subSetIndex].size() == 1)
    {
        if(subSetIndex > K-1)
        {
            return;
        }

        shiftElements(vec, ++subSetIndex);
        vec[subSetIndex].pop_back();
        return;
    }

    // create each subsequence through backtracking
    int currentItem = vec[subSetIndex].back();
    vec[subSetIndex+1].push_back(currentItem);
    vec[subSetIndex].pop_back();
    shiftElements(vec, subSetIndex);

    vec[subSetIndex].push_back(currentItem);

    // store each result into the global variable
    subsets.push_back(vec);
}

void initKSubset(vector<int> i, int k)
{
    K = k;
    if(i.empty())
    {
        return ;
    }

    vector<vector<int>> tempVec;

    // initialize subset
    tempVec.push_back(i);
    for(int idx = 0 ; idx < k - 1 ; idx++)
    {
        tempVec.push_back(vector<int> ());
    }

    // create all k subsets
    shiftElements(tempVec, 0);
    /**/
    cout << "all sets" << endl;
    for (auto& x : subsets) {
        printSubSet(x);
        std::cout << std::endl;
    }
    /**/

}

vector<vector<int>> calculateWeight()
{
    int minWeight = INT8_MAX;
    vector<vector<int>> minWeightVec;

    for (auto& subset : subsets) 
    {
        int weight = 0;
        for (auto& set: subset) 
        {
            int sumSet = 0;
            for (auto& element: set) 
            {
                sumSet = element + sumSet;
            }
            weight = abs(weight - sumSet);
        }
        if(weight < minWeight)
        {
            minWeight = weight;
            minWeightVec = subset;
        }
    }

    return minWeightVec;
}

void split_k_ways(vector<int> i, int k)
{
    initKSubset(i, k);
    printSubSet(calculateWeight());
}

int main()
{
    vector<int> i = {1,2,3,4};
    int k = 3;
    split_k_ways(i, k);
    return 0;
}
