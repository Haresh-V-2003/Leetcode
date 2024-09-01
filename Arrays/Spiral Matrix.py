'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Solution:'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        ans=[]
        i,j=0,0
        UP,RIGHT,DOWN,LEFT=0,1,2,3
        UPWALL=0
        RIGHTWALL=n
        DOWNWALL=m
        LEFTWALL=-1
        DIRECTION=RIGHT
        while len(ans)<m*n:
            if DIRECTION==RIGHT:
                while j<RIGHTWALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                DIRECTION=DOWN
                RIGHTWALL-=1
            elif DIRECTION==DOWN:
                while i<DOWNWALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                DIRECTION=LEFT
                DOWNWALL-=1
            elif DIRECTION==LEFT:
                while j>LEFTWALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                DIRECTION=UP
                LEFTWALL+=1
            else:
                while i>UPWALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                DIRECTION=RIGHT
                UPWALL+=1
        return ans
