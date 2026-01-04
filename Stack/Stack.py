class Stack:
    def __init__(self,max_size) -> None:
        self.__max_size = max_size
        self.__element = [None]*self.__max_size
        self.__top = -1

    def isFull(self):
        if self.__top == self.__max_size - 1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False
    def push(self , val):
        if (self.isFull()):
            print("The stack is full")
        else:
            self.__top = self.__top + 1
            self.__element[self.__top] = val
            print("Element {} is pushed in to the stack".format(val))
    def pop(self):
        if (self.isEmpty()):
            print("The stack is Empty")
        else:
            temp = self.top()
            self.__top = self.__top - 1
            print("element {} popped from the stack".format(temp))
            return temp
    def top(self):
        return self.__element[self.__top]

    def max_size(self):
        return self.__max_size
    
    def display(self):
        if (self.isEmpty()):
            print("There is nothing in the stack..")
        else:
            print("The stack elements are : ", end = " " )
            for i in range(self.__top+1):
                print(self.__element[i],end=' ')
            print()

        print()
n = int(input("Enter maximum size of the stack :  "))
s = Stack(n)
while(True):
    x = int(input("Enter a number :"))
    print()
    if (x == 1):
        val = int(input("Enetr value to be pushed : "))
        s.push(val)
    elif(x == 2):
        s.pop()
    elif(x == 3):
        print("The Stack is Empty",s.isEmpty())
    elif(x == 4):
        print("The stack is full", s.isFull())
    elif(x == 5):
        print("The top element of the stack is : " , s.top())
    elif(x == 6):
        print("the maximum size of the stack is " , s.max_size())
    elif(x == 7):
        s.display()
    elif(x==8):
        print()
        break

        
