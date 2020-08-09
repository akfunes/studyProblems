# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        i = 0
        j = len(nums)-1
        left = [1]
        right = [1]
        left.append(nums[i])
        right.append(nums[j])
        i +=1
        j -=1
        while i < len(nums)-1:

            left.append(left[i]*nums[i])
            right.append(right[i]*nums[j])

            i +=1
            j -=1

        for k in range(len(left)):
            ans.append(left[k] * right[len(right)-1-k])
        return ans
