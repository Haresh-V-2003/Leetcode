'''Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

Solution:'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest=float('inf')
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lo=i+1
            hi=n-1
            while lo<hi:
                current=nums[i]+nums[lo]+nums[hi]
                if abs(current-target)<abs(closest-target):
                    closest=current
                if current==target:
                    return current
                elif current<target:
                    lo+=1
                else:
                    hi-=1
        return closest
