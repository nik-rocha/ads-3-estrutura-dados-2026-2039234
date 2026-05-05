class Queue:
    
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        return self.elements == []
    
    def enqueue(self, item):
        self.elements.insert(0, item)
        
    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
    
    def show(self):
        for i, element in enumerate(self.elements):
            if i == 0:
                print(f"INÍCIO -> {element}", end="")
            elif i == (len(self.elements) - 1):
                print(f" -> {element} <- FIM\n", end="")
            else:
                print(f" -> {element}", end="")
            
fila = Queue()
fila.enqueue("Trilha 1")
fila.enqueue("Trilha 2")
fila.enqueue("Trilha 3")
fila.enqueue("Trilha 4")
fila.show()

print(f"Fila está vazia?: {fila.isEmpty()}")
print(f"Próxima trilha para chegar: {fila.elements[len(fila.elements) -1]}")
print(f"Quantidade de trilhas restantes: {fila.size()}")