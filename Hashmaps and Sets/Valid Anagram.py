'''Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Solution:'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter={}
        if len(s)!=len(t):
            return False
        for a in s:
            if a in counter:
                counter[a]+=1
            else:
                counter[a]=1
        for b in t:
            if b not in counter:
                return False
            elif counter[b]==1:
                del counter[b]
            else:
                counter[b]-=1
        return True
