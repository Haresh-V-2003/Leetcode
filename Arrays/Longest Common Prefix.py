'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

Solution:'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=float('inf')
        for s in strs:
            if len(s)<min_len:
                min_len=len(s)
        i=0
        while i<min_len:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]
