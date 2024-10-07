'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

Solution:'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stk=[]
        maxarea=0
        for i,height in enumerate(heights):
            start=i
            while stk and height<stk[-1][0]:
                h,j=stk.pop()
                w=i-j
                a=w*h
                maxarea=max(maxarea,a)
                start=j
            stk.append((height,start))
        while stk:
            h,j=stk.pop()
            w=n-j
            maxarea=max(maxarea,h*w)
        return maxarea
