'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Solution:'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}
        for m in magazine:
            if m in counter:
                counter[m]+=1
            else:
                counter[m]=1
        for r in ransomNote:
            if r not in counter:
                return False
            elif counter[r]==1:
                del counter[r]
            else:
                counter[r]-=1
        return True
