class Queue:
    def __init__(self):
        self.item = []
    def enqueue(self,value):
        self.item.append(value)
    def dequeue(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.item == []