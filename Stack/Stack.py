class Stack:
    def __init__(self):
        self.stack = []

    def push(self , x):
        self.stack.append(x)
    
    def isEmpty(self):
        if (len(self.stack )== 0):
            return True
        return False
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return ("Stack is empty")
    def Top(self):
        return self.stack[-1]
    
    def size(self):
        return (len(self.stack))
    
    
    
''' Create an object for stack class... '''

s = Stack()

print(s.isEmpty())

s.push(20)
s.push(30)
s.push(35)
s.push(45)

print(s.stack)

print(s.Top())

print(s.size())
print(s.pop())

print (s.stack)
print(s.isEmpty())