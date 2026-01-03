class Node:
    def __init__(self , data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self ):
        self.head = None

    def insert_at_beginning(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self , data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
    def insert_at_loc(self , data , prev):
        temp = self.head
        for i in range(prev-1):
            temp = temp.next
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # delete element...
    def delete_from_beginning(self):
        if(self.head is None):
            print("List is empty")
        else:
            self.head = self.head.next
    def delete_from_end(self):
        if(self.head is None):
            print("List is empty")
        else:
            node = self.head
            while(node.next.next is not None):
                node = node.next
            node.next = None
    def delete_from_loc(self , loc):
        if(self.head == None):
            print("List is empty")
        else:
            temp = self.head
            for i in range(loc-2):
                temp = temp.next
            temp.next = temp.next.next   
    def display(self):
        node = self.head
        while(node is not None):
            print(node.data , end = " ")
            node = node.next
        print()
    def search(self,data):
        node = self.head
        count=0
        while(node):
            if(node.data==data):
                print(data," found at ",count+1,"location .")    
                return
            node = node.next
            count += 1
        print(data , "not found ")
        


l1 = [int(i)  for i in input().split()]      
ll1 = LinkedList()
for i in l1:
    ll1.insert_at_end(i)
ll1.display()

# ll1.insert_at_beginning(10)
print()
ll1.delete_from_loc(1)
ll1.display()
ll1.delete_from_beginning()
ll1.display()
ll1.search(5)
ll1.search(30)
ll1.insert_at_beginning(65)
ll1.display()