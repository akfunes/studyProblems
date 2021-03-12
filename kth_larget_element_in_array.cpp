// https://leetcode.com/problems/kth-largest-element-in-an-array/
#include <algorithm>
#include <iostream>
class Solution {
public:
    void printVec(vector<int>& nums) {
        for (int n:nums) {
            std::cout << n << " " ;
        }
    }
    
    int findKthLargest(vector<int>& nums, int k) {
        std::make_heap(nums.begin(),nums.end());
        
        for (int i = 0 ; i < k-1 ; i++) {
            std::pop_heap(nums.begin(), nums.end());
            nums.pop_back();
        }
        return nums.front();
        
    }
};
