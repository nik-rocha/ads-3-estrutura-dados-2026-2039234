# ## Prática Rápida

# class Queue:
    
#     def __init__(self):
#         self.elements = []
        
#     def isEmpty(self):
#         return self.elements == []
    
#     def enqueue(self, item):
#         self.elements.insert(0, item)
        
#     def dequeue(self):
#         return self.elements.pop()
    
#     def size(self):
#         return len(self.elements)
    
#     def show(self):
#         for i, element in enumerate(self.elements):
#             if i == 0:
#                 print(f"INÍCIO -> {element}", end="")
#             elif i == (len(self.elements) - 1):
#                 print(f" -> {element} <- FIM\n", end="")
#             else:
#                 print(f" -> {element}", end="")
                
# fila = Queue()
# fila.enqueue(100)
# fila.enqueue(200)
# fila.enqueue(300)
# fila.enqueue(400)
# fila.show()

# fila.dequeue()
# fila.dequeue()
# fila.show()

# fila.enqueue(500)
# fila.enqueue(600)
# fila.show()

# 1. Atendimento na Recepção

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
                print(f"{element}, ", end="")
            elif i == (len(self.elements) - 1):
                print(f"{element}\n", end="")
            else:
                print(f"{element}, ", end="")
                
fila = Queue()
fila.enqueue("Ana")
fila.enqueue("Bruno")
fila.enqueue("Carlos")
fila.enqueue("Diana")
print(f"Entrada: ", end="")
fila.show()

print(f"Saída: {fila.dequeue()}, {fila.dequeue()}")
fila.show()

print(f"Entrada: ", end="")
fila.show()