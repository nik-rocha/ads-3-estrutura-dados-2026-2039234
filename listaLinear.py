class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return f"[{self.data}]->"
    
# Exemplo de nós encadeados
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

head = n1
n1.next = n2
n2.next = n3

# Percorrer a lista
while head is not None:
    print(head, end="")
    head = head.next
    
    
# ### Caminhando e Somando

# Você recebeu uma sequência de números e precisa calcular a soma total. Use lista encadeada.

# * Crie 8 nós
# * Encadeie os nós (cada nó aponta para o próximo)
# * Percorra usando while
# * Mostre a soma final
# * Mostra a sequência de números

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return f"[{self.data}]->"

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

def sumNodes(h):
    sumN = 0
    
    while h is not None:
        sumN += h.data
        h = h.next
    
    print(sumN)
        
sumNodes(head)

while head is not None:
    print(head, end="")
    head = head.next
    
# ### Sendo uma pessoa organizada

# Você está monstando uma fila de tarefas. Precisa inserir novas tarefas na sua lista, porém quer dividir em tarefas com prioridades e tarefas normais. Não existe diferença entre normal e prioridade, porém toda tarefa com prioridade é inserida no começo da fila e tarefas normais, inseridas no final da fila.

# * Crie a classe Node
# * Crie uma função add_list()
# * Crie uma função add_last()
# * Crie uma função show_tasks()

# **Dica:** `head` representa o começo da lista, um elemento é o último quando seu `next` é _None_

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 
        
    def __repr__(self):
        return f"[{self.data}]->"
    
def add_first(head, task):
    new = Node(task)
    new.next = head
    return new    

def add_last(head, task):
    new = Node(task)
    
    if head is None:
        return new
    
    last = head
    while last.next is not None:
        last = last.next
        
    last.next = new
    return head

def show_tasks(head):
    task = head
    
    while task is not None:
        if task.next is None:
           print(f"{task}None")
        else:
            print(task)
        task = task.next
    
head = None    

head = add_first(head, "Tarefa 1")
head = add_last(head, "Tarefa 2")
show_tasks(head)

