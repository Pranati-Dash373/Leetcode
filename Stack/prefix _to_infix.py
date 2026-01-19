class Solution :
    def prefixtoinfix(self , exp):
        stack = []
        for i in range (len(exp)-1 , -1 , -1 ):
            if (exp[i] >= 'A' and exp[i] <= 'Z' ) or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
                stack.append(exp[i])
            elif exp[i] in "+-*/^":
                if len(stack) < 2:
                    return "Invalid prefix expression"
                t1 = stack[-1]
                stack.pop()
                t2 = stack[-1]
                stack.pop()
                res = "(" + t1 + exp[i] + t2 + ")"
                stack.append(res)
        if len(stack) != 1 :
            return "Invalid prefix expression"

        return stack[-1]
    
if __name__ == '__main__':
    obj = Solution()
    exp1 = input("Enter prefix expression : ")
    print(obj.prefixtoinfix(exp1))
    

'''
Prefix :*+PQ-MN

infix : ((P+Q)*(M-N))

'''