'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

Solution:'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindist=[float('inf')]
        prev=[None]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if prev[0] is not None:
                mindist[0]=min(mindist[0],node.val-prev[0])
            prev[0]=node.val
            dfs(node.right)
        dfs(root)
        return mindist[0]
