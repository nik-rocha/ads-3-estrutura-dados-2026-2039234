# # ### Exercício 1 - Limpeza de Dados Duplicados

# # Descrição: Um sistema registrou eventos em uma sequência encadeada com possíveis
# # duplicações. Seu objetivo é limpar essa estrutura.
# # Regras:
# # - Não utilizar estruturas auxiliares (listas, sets, etc.)
# # - Trabalhar apenas com ponteiros (proximo)
# # - Manter a primeira ocorrência e preservar a ordem

# class Node:
    
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.previous = None
        
#     def __repr__(self):
#         return f"[{self.data}]<->"
    
# def clean_list(head):
#     current = head
    
#     while current is not None:
#         finder = current
        
#         while finder.next is not None:
#             if finder.next.data == current.data:
#                 equal_value = finder.next
#                 finder.next = equal_value.next
                
#                 if equal_value.next is not None:
#                     equal_value.next.previous = finder
#             else:
#                 finder = finder.next
                
#         current = current.next
        
#     return head

# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next
    
# n1 = Node(5)
# n2 = Node(3)
# n3 = Node(5)
# n4 = Node(2)
# n5 = Node(3)
# n6 = Node(1)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

# n2.previous = n1
# n3.previous = n2
# n4.previous = n3
# n5.previous = n4
# n6.previous = n5

# show_list(head)

# clean_list(head)

# show_list(head)

# ### Exercício 2 — Reorganização de Segmento

# # Descrição: Uma fila precisa ter parte de seus elementos reorganizados invertendo um trecho
# # específico.
# # Regras:
# # - Não criar uma nova lista
# # - Manipular apenas os ponteiros
# # - Considerar índice iniciando em 0

# class Node:
    
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.previous = None
        
#     def __repr__(self):
#         if self.next == None:
#             return f"[{self.data}]"
#         else:
#             return f"[{self.data}] <-> "
    
# def reverse_section(head, i, j):
#     current = head
#     index = 0
    
#     while current and index < i:
#         current = current.next
#         index += 1
    
#     if not current: 
#         return head
            
#     before_start = current.previous
#     section_start = current
    
#     last = None
#     while current and index <= j:
#         last = current.previous
#         current.previous = current.next 
#         current.next = last
        
#         current = current.previous
#         index += 1
        
#     last_node = last.previous
    
#     if before_start:
#         before_start.next = last_node
#     else:
#         head = last_node
        
#     last_node.previous = before_start
#     section_start.next = current
    
#     if current:
#         current.previous = section_start
        
#     return head
            
# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next
        
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

# n2.previous = n1
# n3.previous = n2
# n4.previous = n3
# n5.previous = n4
# n6.previous = n5

# reverse_section(head, 2, 4)
# show_list(head)

# ### Exercício 3 — Busca com Otimização

# # Descrição: Comparar busca em lista encadeada desordenada e ordenada.
# # Regras:
# # - Implementar duas estratégias de busca
# # - Contar número de passos
# # - Na lista ordenada, interromper a busca antecipadamente quando possível

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        if self.next is None:
            return f"[{self.data}]"
        else:
            return f"[{self.data}]->"

class Unordened:
    
    def __init__(self):
        self.head = None
        
    def add(self, i):
        new = Node(i)
        new.next = self.head
        self.head = new
        
        return new        
            
    def search(self, i):
        current = self.head
        x = 0
        p = 0
        
        while current is not None:
            
            if current.data == i:
                x += 1
                
            p += 1
            current = current.next
            
        if x == 0:
            print(f"O valor {i} não foi encontrado. Foram percorridos {p} passos (a lista toda).")
        else:
            print(f"O valor {i} foi encontrado! Foram percorridos {p} passos (a lista toda).")
            
        return self.head
    
    def show_list(self):
        current = self.head
        while current is not None:
            print(current, end="")
            current = current.next
        print()
            
class Ordened:
    
    def __init__(self):
        self.head = None
        
    def add(self, i):
        new = Node(i)
        
        if self.head is None or self.head.data >= i:
            self.head = new
            return
        
        current = self.head
        
        while current.next is not None and current.next.data < i:
            current = current.next 
            
        current.next = new   
        
    def search(self, i):
        current = self.head
        p = 0
        
        while current is not None:
            if current.data == i:
                print(f"O valor {i} foi encontrado! Foram percorridos {p} passos.")
                return
                
            p += 1
            current = current.next
            
        print(f"O valor {i} não foi encontrado. Foram percorridos {p} passos.")
        
        return self.head
            
    def show_list(self):
        current = self.head
        while current is not None:
            print(current, end="")
            current = current.next
        print()

unordened_list = Unordened()

unordened_list.add(1)
unordened_list.add(2)
unordened_list.add(3)
unordened_list.add(4)
unordened_list.show_list()
unordened_list.search(3)

ordened_list = Ordened()

ordened_list.add(1)
ordened_list.add(2)
ordened_list.add(3)
ordened_list.add(4)
ordened_list.show_list()
ordened_list.search(3)

### Exercício 4 — Identificação de Elementos em Comum

# Descrição: Identificar elementos que aparecem em duas listas encadeadas.
# Regras:
# - Não utilizar estruturas auxiliares
# - Não repetir valores na lista final
# - Preservar a ordem da primeira lista

#