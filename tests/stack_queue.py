
class Stack:
    def __init__(self):
        self.elements = []

    def print(self):
        print(self.elements)

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        self.elements.pop()


class Queue:
    def __init__(self):
        self.items = [] 

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)
    
