# # 1 - Crie uma função mostrar_lista(head) que percorra a lista encadeada e mostre todos os valores na
# # tela, um por linha. Teste com a lista: 7 -> 14 -> 21 -> 28.

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
        
#     def __repr__(self):
#         return f"[{self.data}]->"
    
# n1 = Node(7)    
# n2 = Node(14)    
# n3 = Node(21)    
# n4 = Node(28)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4

# def show_list(head):
#     while head is not None:
#         print(head)
#         head = head.next
        
# show_list(head)
        
# # 2- Crie uma função inserir_fim(head, valor) que adicione um novo nó no final da lista. Teste inserindo
# # os valores 10, 20 e 30, nessa ordem. Depois, mostre a lista completa.

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
        
#     def __repr__(self):
#         return f"[{self.data}]->"

# head = None

# def add_last(head, n):
#     new = Node(n)
    
#     if head is None:
#         return new
    
#     last = head
    
#     while last.next is not None:
#         last = last.next
        
#     last.next = new
#     return head

# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next
        
# head = add_last(head, 10)
# show_list(head)
# head = add_last(head, 20)
# head = add_last(head, 30)
# show_list(head)

# # 3- Crie uma função buscar(head, alvo) que retorne True se o valor existir e False caso contrário. Teste
# # com a lista: 4 -> 9 -> 12 -> 18. Verifique os valores 12 e 5.

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
        
#     def __repr__(self):
#         return f"[{self.data}]->"

# n1 = Node(4)    
# n2 = Node(9)    
# n3 = Node(12)    
# n4 = Node(18)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4

# def find_item(head, alvo):
#     while head is not None:
#         if head.data == alvo:
#             print(f"O valor {alvo} foi encontrado!")
#             return True
        
#         head = head.next
        
#     print(f"O valor {alvo} não foi encontrado.")
#     return False

# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next
        
# show_list(head)
# find_item(head, 18)

# # 4- Crie uma função contar(head, alvo) que conte quantas vezes um valor aparece na lista. Teste com a
# # lista: 3 -> 6 -> 3 -> 9 -> 3 -> 12. Conte o valor 3 e depois o valor 8.

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
        
#     def __repr__(self):
#         return f"[{self.data}]->"

# n1 = Node(3)    
# n2 = Node(6)    
# n3 = Node(9)    
# n4 = Node(3)
# n5 = Node(12)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# def count_data(head, data):
#     i = 0
    
#     while head is not None:
#         if head.data == data:
#             i += 1
            
#         head = head.next
        
#     print(f"\nO valor {data} foi encontrado {i} vez(es) em sua lista encadeada.")

# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next
        
# show_list(head)
# count_data(head, 3)
# count_data(head, 8)

# # Monte uma lista encadeada com os valores 5, 10, 5 e 20. Em seguida:
# #  a) mostre a lista;
# #  b) insira o valor 30 no fim;
# #  c) busque o valor 10;
# #  d) conte quantas vezes o valor 5 aparece.
# # No final, mostre novamente a lista e os resultados das operações.

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
        
#     def __repr__(self):
#         return f"[{self.data}]->"

# n1 = Node(5)    
# n2 = Node(10)    
# n3 = Node(5)    
# n4 = Node(20)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4

# def show_list(head):
#     while head is not None:
#         print(head, end="")
#         head = head.next

# def add_last(head, n):
#     new = Node(n)
    
#     if head is None:
#         return new
    
#     last = head
    
#     while last.next is not None:
#         last = last.next
        
#     last.next = new
#     return head

# def find_item(head, alvo):
#     while head is not None:
#         if head.data == alvo:
#             print(f"\nO valor {alvo} foi encontrado!")
#             return True
        
#         head = head.next
        
#     print(f"\nO valor {alvo} não foi encontrado.")
#     return False

# def count_data(head, data):
#     i = 0
    
#     while head is not None:
#         if head.data == data:
#             i += 1
            
#         head = head.next
        
#     print(f"\nO valor {data} foi encontrado {i} vez(es) em sua lista encadeada.")
    
# show_list(head)
# add_last(head, 30)
# find_item(head, 10)
# count_data(head, 5)
# show_list(head)

# Uma pequena loja quer registrar os códigos dos produtos que chegaram no dia usando uma lista
# encadeada simples. Seu programa deve interpretar a situação e decidir quais funções criar. A loja
# precisa:
#  a) montar a lista inicial com os códigos 101, 205, 101 e 330;
#  b) mostrar todos os códigos cadastrados;
#  c) inserir no fim o código 450, referente a um novo produto recebido;
#  d) verificar se o código 205 está presente na lista;
#  e) contar quantas vezes o código 101 aparece, pois esse produto chegou em mais de uma caixa.
# Mostre a lista final e os resultados das verificações.

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return f"[{self.data}]->"

c1 = Node(101)    
c2 = Node(205)    
c3 = Node(101)    
c4 = Node(330)

head = c1
c1.next = c2
c2.next = c3
c3.next = c4

def show_codes(head):
    while head is not None:
        print(head, end="")
        head = head.next

def add_last_code(head, n):
    new = Node(n)
    
    if head is None:
        return new
    
    last = head
    
    while last.next is not None:
        last = last.next
        
    last.next = new
    return head

def find_code(head, codigo):
    while head is not None:
        if head.data == codigo:
            print(f"\nO código {codigo} foi encontrado!")
            return True
        
        head = head.next
        
    print(f"\nO código {codigo} não foi encontrado.")
    return False

def count_code(head, data):
    i = 0
    
    while head is not None:
        if head.data == data:
            i += 1
            
        head = head.next
        
    print(f"\nO código {data} foi encontrado {i} vez(es) nos produtos.")
    
show_codes(head)
add_last_code(head, 450)
find_code(head, 205)
count_code(head, 101)
show_codes(head)