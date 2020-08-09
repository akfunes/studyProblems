# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) <= 1):
            return

        i = len(nums)-2
        found = False
        while not found and i >= 0:
            n1 = nums[i]
            n2 = nums[i+1]

            if n1 < n2:
                j = len(nums)-1
                n2 = nums[j]
                while n2 <= n1 and j > 0:
                    j -=1
                    n2 = nums[j]
                nums[j] = n1
                nums[i] = n2
                found = True
            i -=1
        if not found:
            nums.sort()
        else:
            print(nums)
            print(nums[i+2:])
            nums[i+2:] = sorted(nums[i+2:])
