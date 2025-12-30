'''
Docstring for Sum_of_beauty_of_all_substring

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
 
'''

class Solution:
    def beautySum(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i , len(s)):
                freq[s[j]] = freq.get((s[j]) , 0) + 1
                count += max(freq.values()) - min(freq.values()) 
        return count