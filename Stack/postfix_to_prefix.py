class Solution :
    def postfixtoprefix(self , exp):
        stack = []
        for i in range (len(exp)):
            if (exp[i] >= 'A' and exp[i] <= 'Z' ) or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
                stack.append(exp[i])
            elif exp[i] in "+-*/^":
                if len(stack) < 2:
                    return "Invalid Postfix expression"
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                res =  exp[i] + t2 + t1 
                stack.append(res)
        if len(stack) != 1 :
            return "Invalid postfix expression"

        return stack[-1]
    
if __name__ == '__main__':
    obj = Solution()
    exp1 = input("Enter postfix expression : ")
    print(obj.postfixtoprefix(exp1))

'''
postfix : AB-DE+F*/

prefix : /-AB*+DEF

'''