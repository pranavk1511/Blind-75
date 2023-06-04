
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        ans=[-1,-1]
        for x in range(len(nums)):
            if nums[x]==target:
                ans[0]=x
                break
        for x in range(len(nums)-1,-1,-1):
            if nums[x]==target:
                ans[1]=x
                break
        return ans