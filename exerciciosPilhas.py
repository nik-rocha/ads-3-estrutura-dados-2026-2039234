# # 1) Caixas no Deposito

# class Stack:
    
#     def __init__(self):
#         self.deposit = []
#         self.removed = []
#         self.last_removal = None
        
#     def isEmpty(self):
#         return self.deposit == []
    
#     def push(self, item):
#         self.deposit.append(item)
        
#     def pop(self):
#         self.last_removal = self.deposit.pop()
#         return self.removed.append(self.last_removal)
    
#     def peek(self):
#         return self.deposit[len(self.deposit)-1]
    
#     def size(self):
#         return len(self.deposit)
    
# deposito = Stack()
# deposito.push(1)
# deposito.push(2)
# deposito.push(3)
# deposito.push(4)

# print(f"Pilha atual: {deposito.deposit}")

# deposito.pop()
# deposito.pop()

# print(f"Removidos: {deposito.removed}")
# print(f"Último removido: {deposito.last_removal}")
# print(f"Pilha final: {deposito.deposit}")

# # 2) Mesa de Livros

# class Stack:
    
#     def __init__(self):
#         self.library = []
#         self.last_removal = None
        
#     def isEmpty(self):
#         return self.library == []
    
#     def push(self, item):
#         self.library.append(item)
        
#     def pop(self):
#         self.last_removal = self.library.pop()
#         return self.last_removal
    
#     def peek(self):
#         return self.library[len(self.library)-1]
    
#     def size(self):
#         return len(self.library)
    
# biblioteca = Stack()
# biblioteca.push("Python")
# biblioteca.push("Algoritmos")
# biblioteca.push("Estruturas de Dados")

# print(f"Pilha: {biblioteca.library}")
# print(f"Topo inicial:")
# print(biblioteca.peek())

# biblioteca.pop()

# print(f"Removido: {biblioteca.last_removal}")
# print(f"Novo topo: {biblioteca.peek()}")

# # 3) Palavra Invertida

# class Stack:
    
#     def __init__(self, word:str):
#         self.word = word
#         self.letters = []
        
#     def isEmpty(self):
#         return self.letters == []
    
#     def push(self, item):
#         self.letters.append(item)
        
#     def pop(self):
#         return self.letters.pop()
    
#     def peek(self):
#         return self.letters[len(self.letters)-1]
    
#     def size(self):
#         return len(self.letters)
    
#     def reverse(self):
#         reversed = ""
#         while not self.isEmpty():
#             reversed += self.pop()
#         return reversed
    
# palavra = Stack("python")

# for letter in palavra.word:
#     palavra.letters.append(letter)

# palavra.reverse()

# # 4) Palavra Palindroma

# class Stack:
    
#     def __init__(self, word:str):
#         self.word = word
#         self.letters = []
        
#     def isEmpty(self):
#         return self.letters == []
    
#     def push(self, item):
#         self.letters.append(item)
        
#     def pop(self):
#         return self.letters.pop()
    
#     def peek(self):
#         return self.letters[len(self.letters)-1]
    
#     def size(self):
#         return len(self.letters)
    
#     def palindrome_verify(self):
#         palindrome = ""
#         while not self.isEmpty():
#             palindrome += self.pop()
        
#         if self.word == palindrome:
#             print("Sua palavra é um palíndromo!")
#             return True
#         else:
#             print("Sua palavra não é um palíndromo.")
#             return False
    
# palavra = Stack("arara")

# for letter in palavra.word:
#     palavra.letters.append(letter)

# palavra.palindrome_verify()

# # 5) Botao Voltar

# class Stack:
    
#     def __init__(self):
#         self.history = []
        
#     def isEmpty(self):
#         return self.history == []
    
#     def push(self, item):
#         self.history.append(item)
        
#     def pop(self):
#         return self.history.pop()
    
#     def peek(self):
#         return self.history[len(self.history)-1]
    
#     def size(self):
#         return len(self.history)
    
#     def return_page(self):
#         current_page = self.pop()
#         print(f"Você saiu de {current_page} e voltou para {self.peek()}.")
    
# navegador = Stack()
# navegador.push("google.com")
# navegador.push("youtube.com")
# navegador.push("github.com")

# print(f"\nTopo atual: {navegador.peek()}")
# navegador.return_page()
# print(f"\nTopo atual: {navegador.peek()}")
# navegador.return_page()
# print(f"\nTopo atual: {navegador.peek()}")

# # 6) Desfazer na Calculadora

# class Stack:
    
#     def __init__(self):
#         self.calculator = []
        
#     def isEmpty(self):
#         return self.calculator == []
    
#     def push(self, item):
#         self.calculator.append(item)
        
#     def pop(self):
#         value = self.calculator.pop()
#         return print(f"O valor {value} foi removido.")
    
#     def peek(self):
#         return self.calculator[len(self.calculator)-1]
    
#     def size(self):
#         return len(self.calculator)
    
#     def sum(self):
#         sum_value = 0
#         for numero in self.calculator:
#             sum_value += numero
            
#         return print(f"A soma dos número é: {sum_value}")    
    
# calculadora = Stack()
# calculadora.push(10)
# calculadora.push(20)
# calculadora.push(30)

# print(f"Pilha atual: {calculadora.calculator}")
# calculadora.sum()
# calculadora.pop()
# print(f"\nPilha atual: {calculadora.calculator}")
# calculadora.sum()

# # 7) Torre de Blocos

# class Stack:
    
#     def __init__(self):
#         self.blocks = []
        
#     def isEmpty(self):
#         return self.blocks == []
    
#     def push(self, item):
#         self.blocks.append(item)
        
#     def pop(self):
#         return self.blocks.pop()
    
#     def peek(self):
#         return self.blocks[len(self.blocks)-1]
    
#     def size(self):
#         return len(self.blocks)
    
#     def remove_smaller(self):
#         temp_stack = []
        
#         while not self.isEmpty():
#             item = self.pop()
            
#             if item >= 4:
#                 temp_stack.append(item)
                
#         while len(temp_stack) > 0:
#             self.push(temp_stack.pop())
            
#         return self.blocks
    
# torre = Stack()
# torre.push(5)
# torre.push(3)
# torre.push(8)
# torre.push(2)
# torre.remove_smaller()

# # 8) Histórico do Editor

# class Stack:
    
#     def __init__(self):
#         self.edit_history = []
#         self.undone = []
        
#     def isEmpty(self):
#         return self.edit_history == []
    
#     def push(self, item):
#         self.edit_history.append(item)
        
#     def pop(self):
#         return self.edit_history.pop()
    
#     def peek(self):
#         return self.edit_history[len(self.edit_history)-1]
    
#     def size(self):
#         return len(self.edit_history)
    
#     def undo(self):
#         action = self.pop()
#         self.undone.append(action)
        
#         return print(f"Ações desfeitas: {self.undone}")
    
#     def show(self):
#         print(self.edit_history)
    
# edicao = Stack()
# edicao.push("digitar A")
# edicao.push("digitar B")
# edicao.push("apagar")
# edicao.push("colar")
# edicao.show()

# edicao.undo()
# edicao.undo()
# edicao.show()

# # 9) Validador de Parenteses

# class Stack:
    
#     def __init__(self):
#         self.items = []
        
#     def isEmpty(self):
#         return self.items == []
    
#     def push(self, item):
#         self.items.append(item)
        
#     def pop(self):
#         return self.items.pop()
    
#     def peek(self):
#         return self.items[len(self.items)-1]
    
#     def size(self):
#         return len(self.items)
        
#     def bracket_verifier(self):
#         temp = [] 
        
#         while not self.isEmpty():
#             character = self.pop()
#             if character == ")":
#                 temp.append(")")
#             elif character == "(":
#                 if len(temp) == 0:
#                     return "Inválida"
#                 temp.pop()
        
#         if len(temp) == 0:
#             return "Válida"
#         else:
#             return "Inválida"
            
# calculo = Stack()
# calculo.push("(a _+ b) * (c + d)")
# calculo.bracket_verifier()

# # 10) Filtrando Valores Pares

# class Stack:
    
#     def __init__(self):
#         self.values = []
        
#     def isEmpty(self):
#         return self.values == []
    
#     def push(self, item):
#         self.values.append(item)
        
#     def pop(self):
#         return self.values.pop()
    
#     def peek(self):
#         return self.values[len(self.values)-1]
    
#     def size(self):
#         return len(self.values)
    
#     def remove_odds(self):
#         temp_stack = []
        
#         while not self.isEmpty():
#             item = self.pop()
            
#             if item % 2 == 0:
#                 temp_stack.append(item)
                
#         while len(temp_stack) > 0:
#             self.push(temp_stack.pop())
            
#         return self.values
    
# quantia = Stack()
# quantia.push(1)
# quantia.push(2)
# quantia.push(3)
# quantia.push(4)
# quantia.push(5)
# quantia.push(6)
# print(quantia.values)
# quantia.remove_odds()

# 11) Desafio - Mensagem Secreta

class Stack:
    
    def __init__(self):
        self.codes = []
        
    def isEmpty(self):
        return self.codes == []
    
    def push(self, item):
        self.codes.append(item)
        
    def pop(self):
        return self.codes.pop()
    
    def peek(self):
        return self.codes[len(self.codes)-1]
    
    def size(self):
        return len(self.codes)
    
    def decodifY(self):
        temp_stack = []

        while not self.isEmpty():
            code = self.pop()
            for character in code:
                if character == "#":
                    if temp_stack:
                        temp_stack.pop()
                
                else:
                    temp_stack.append(character)
                    
        decoded = "".join(temp_stack)
        self.push(decoded)

        return print(f"Seu código decodificado é: {self.codes}")
    
mensagem = Stack()
mensagem.push("ABC#D##E")
mensagem.decodifY()