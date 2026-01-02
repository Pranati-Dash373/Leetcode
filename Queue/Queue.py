class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self , x):
        self.queue.append(x)

    def isEmpty(self):
        if (len(self.queue) == 0):
            return True
        return False
    
    def deQueue(self):
        if not self.isEmpty():
            return (self.queue.pop(1))
        return ("Queue is empty")
    
    def Front(self):
        return (self.queue[0])
    
    def rare(self):
        return (self.queue[-1])
    
    def size(self):
        return (len(self.queue))
    
''' Create an object foe queue.. '''


q = Queue()

print(q.queue)

q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)

print(q.queue)

print(q.isEmpty())

print(q.deQueue())

print(q.Front())

print(q.rare())

print(q.size())

print(q.queue)