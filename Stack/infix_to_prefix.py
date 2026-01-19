class Solution:
    def priority(self , c):
        if c == '^' :
            return 3
        elif c == '*' or c == '%':
            return 2
        elif c == '(+' or c == '-':
            return 1
        else:
            return -1
    def infixtoprefix(self , str):
        stack = []
        res = ""
        rev = ""
        for ch in reversed(str):
            if ch == '(':
                rev += ')'
            elif ch == ')':
                rev += '('
            else:
                rev += ch

        for i in  range(len(rev)) :
            if (rev[i] >= 'A' and rev[i] <= 'Z') or (rev[i] >= 'a' and rev[i] <= 'z') or (rev[i] >= '0' and rev[i] <= '9'):
                res += rev[i]
            elif rev[i] == '(':
                stack.append(rev[i])
            elif rev[i] == ')' :
                while stack and stack[-1] != '(' :
                    res += stack[-1]
                    stack.pop()
                stack.pop()
            elif rev[i] == '^':
                while stack and self.priority(rev[i]) == self.priority(stack[-1]):
                    res += stack[-1]
                    stack.pop()
                stack.append(rev[i])
            else:
                while stack and self.priority(rev[i]) < self.priority(stack[-1]):
                    res += stack[-1]
                    stack.pop()
                stack.append(rev[i])

        while stack :
            res += stack[-1]
            stack.pop()
        

        return res[::-1]
    
if __name__ == '__main__':
    obj = Solution()
    str1 = input("Enter Infix expression : ")
    print(obj.infixtoprefix(str1))


'''

infix : (A+B)*C-D+F

prefix : +-*+ABCDF

'''