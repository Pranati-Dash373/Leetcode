class Queue:
    def __init__(self , max_size):
        self.__max_size = max_size
        self.__element = [None]*max_size
        self.__front = 0
        self.__rare = -1
    def isFull(self):
        if (self.__rare == self.__max_size -1):
            return True
        return False
    def isEmpty(self):
        if (self.__front > self.__rare):
            return True
        return False
    def front(self):
        return self.__element[self.__front]
    def enqueue(self , val):
        if (self.isFull()):
            print("The Queue is full so can't insert element..")
        else:
            self.__rare += 1
            self.__element[self.__rare] = val
            print("The {} element is inserted in the queue".format(val))

    def dequeue(self):
        if(self.isEmpty()):
            print("The queue is empty , so can't remove element from the queue.. ")
        else:
            temp = self.__element[self.__front]
            self.__element[self.__front] = None
            self.__front += 1
            print("the {} element is removed from the queue..".format(temp))
            return temp
    def max_size(self):
        return self.__max_size
    def display(self):
        if (self.isEmpty()):
            print("Queue is empty..")
        else:
            print("The elements present in the queue are : ", end = " ")
            for i in range(self.__front , self.__rare+1):
                print(self.__element[i] , end = " ")
            print()

n = int(input("enter Maximun size of the queue :"))
q = Queue(n)
while(True):
    x = int(input("Enter a number : "))
    print()
    if (x==1):
        print("The queue is Empty..",q.isEmpty())
    elif(x==2):
        print("The queue is Full ..", q.isFull())
    elif(x==3):
        val = int(input("Enter value to be inserted : "))
        q.enqueue(val)
    elif(x==4):
        q.dequeue()
    elif(x==5):
        print(" the front value is : " , q.front())
    elif(x==6):
        print("the maximum size of the queue is ", q.max_size())

    elif(x==7):
        q.display()
    elif(x == 8):    
        print()
        break


