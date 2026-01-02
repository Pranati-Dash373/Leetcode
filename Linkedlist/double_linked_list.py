class Node:
    def __init__(self,data=None,next=None,prev=None) -> None:
        self.next=next
        self.prev=prev
        self.data=data
class Doubly_linked_list:
    def __init__(self) -> None:
        self.head=None
# insert elements
    def insert_at_beginning(self,data): 
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node.next

    def insert_at_end(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            new_node.prev=temp
            temp.next=new_node

    def insert_after_loc(self,data,loc):
        new_node=Node(data)
        temp=self.head
        for i in range(loc-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
        new_node.prev=temp
# delete elements..
    def delete_from_beginning(self):
        if(self.head is None):
            print("List is empty")
        else:
            self.head.next.prev=None
            self.head=self.head.next
    def delete_from_end(self):
        if(self.head is None):
            print("Liselft is empty")
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=None
    def delete_by_loc(self,loc):
        if(self.head is None):
            print("List is empty")
        else:
            temp=self.head
            for i in range(loc-1):
                if(temp.next):
                    temp=temp.next
                else:
                    print("Index out of bound")
                    return 
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
# Display
    def display_forward(self):
        if(self.head == None):
            print("List is empty")
        else:
            temp=self.head
            while(temp is not None):
                print(temp.data,end="  ")
                temp=temp.next
            print()

    def no_of_nodes(self):
        count =0
        temp=self.head
        while(temp is not None):
            temp=temp.next
            count+=1
        return count

dl=Doubly_linked_list()
l1=[int(i) for i in input().split()]
for i in l1:
    dl.insert_at_end(i)
dl.display_forward()
dl.insert_after_loc(40,3)
dl.display_forward()
dl.delete_by_loc(10)
print(dl.no_of_nodes())