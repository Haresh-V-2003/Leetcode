'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.

Solution:'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter=defaultdict(int)
        balloon='balloon'
        for s in text:
            if s in balloon:
                counter[s]+=1
        for s in balloon:
            if s not in counter:
                return 0
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
