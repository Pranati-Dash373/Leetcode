'''
Docstring for Valid_paranthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Example 5:

Input: s = "([)]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if(len(a) != 0 and i == ')' and a[-1] == '('):
                a = a[:-1]
            elif(len(a) != 0 and i == '}' and a[-1] == '{'):
                a = a[:-1]
            elif(len(a) != 0 and i == ']' and a[-1] == '['):
                a = a[:-1]
            else:
                a.append(i)
        if(len(a) ==0):
            return True
        return False