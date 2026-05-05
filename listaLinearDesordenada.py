# Desordenada 

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
        
    def set_next(self, next):
        self.next = next
        
class UnorderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        if self.head is None:
            return True
        
        return False
    
    def size(self):
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        
    def append(self, data):
        temp = Node(data)
        
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
            
        current.set_next(temp)
        
    def remove(self, element):
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.get_data() == element:
                found = True
            else:
                previous = current # persistimos sempre o nó anterior para poder mover na lista
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    def search(self, data):
        current = self.head
        found = False
        
        while not found and current != None:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
                
        return found
    
    def show(self):
        current = self.head
        
        while current is not None:
            
            if current.get_next() is not None:
                print(f"{current.get_data()} -> ", end="")
            else:
                print(f"{current.get_data()} -> None")
            current = current.get_next()
            
list = UnorderedList()

list.add(1)
list.show()
list.add(10)
list.show()
list.add(15)
list.show()
list.add(0)
list.show()
list.add(3)
list.show()

# Ordenada

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
        
    def set_next(self, next):
        self.next = next
        
class OrderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def add(self, data):
        current = self.head
        previous = None
        stop = False
        
        while current is not None and not stop:
            if current.get_data() > data:
                stop = True
            else:
                previous = current
                current = current.get_next()
            new = Node(data)
            if previous == None:
                new.set_next(self.head)
                self.head = new
            else:
                new.set_next(current)
                previous.set_next(new)
                
    def remove(self, data):
        current = self.head
        previous = None
        found = False
        
        while not found and current.get_data() < data:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next
                
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
                
    def show(self):
        current = self.head
        
        while current is not None:
            
            if current.get_next() is not None:
                print(f"{current.get_data()} -> ", end="")
            else:
                print(f"{current.get_data()} -> None")
            current = current.get_next()
            
list = OrderedList()

list.add(1)
list.show()
list.add(10)
list.show()
list.add(15)
list.show()
list.add(0)
list.show()
list.add(3)
list.show()