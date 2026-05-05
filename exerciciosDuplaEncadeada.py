# Exercício 1 - Mostrar a lista

# Crie uma lista duplamente encadeada com os valores 3, 6, 9 e 12. Depois, percorra a lista do início
# para o fim e mostre todos os valores na tela, um por linha.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
    def __repr__(self):
        return f"{self.data}"
    
n1 = Node(3)
n2 = Node(3)
n3 = Node(3)
n4 = Node(3)