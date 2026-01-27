class Solution:
    def priority(self , c):
        if c == '^' :
            return 3
        elif c == '*' or c == '%':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1
    def infixtopostfix(self , str):
        stack = []
        res = ""
        for i in  range(len(str)) :
            if (str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= 'a' and str[i] <= 'z') or (str[i] >= '0' and str[i] <= '9'):
                res += str[i]
            elif str[i] == '(':
                stack.append(str[i])
            elif str[i] == ')' :
                while stack and stack[-1] != '(' :
                    res += stack[-1]
                    stack.pop()
                stack.pop()
            else :
                while stack and self.priority(str[i]) <= self.priority(stack[-1]):
                    res += stack[-1]
                    stack.pop()
                stack.append(str[i])

        while stack :
            res += stack[-1]
            stack.pop()

        return res
    
if __name__ == '__main__':
    obj = Solution()
    str1 = input("Enter Infix expression : ")
    print(obj.infixtopostfix(str1))


'''
infix : a+b*(c^d-e)

postfix : abcd^e-*+

'''