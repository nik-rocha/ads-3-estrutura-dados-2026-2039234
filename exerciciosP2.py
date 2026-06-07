# # 1

# class Stack():

#     def __init__(self):
#         self.history = []

#     def isEmpty(self):
#         return self.history == []
    
#     def push(self, item):
#         return self.history.append(item)

#     def pop(self):
#         return self.history.pop()
    
#     def peek(self):
#         return self.history[len(self.history)-1]
    
#     def size(self):
#         return len(self.history)
    
#     def accessPage(self, page):
#         print(f"Você acessou {page}.")
#         return self.push(page)

#     def returnPage(self):
#         current_page = self.pop()
#         print(f"Você saiu de {current_page} e voltou para {self.peek()}.")

#     def showHistory(self):
#         print('Histórico:\n')
#         for page in self.history:
#             print(page)

# historico = Stack()
# historico.accessPage("google.com")
# historico.accessPage("unimar.com")
# historico.accessPage("moodle.unimar.br")
# historico.showHistory()
# print(f"Página atual: {historico.peek()}")

# historico.returnPage()

# print(f"Página atual: {historico.peek()}")
# historico.showHistory()

# 2

# class Stack():

#     def __init__(self):
#         self.expression = []

#     def isEmpty(self):
#         return self.expression == []
    
#     def push(self, item):
#         return self.expression.append(item)
    
#     def pop(self):
#         return self.expression.pop()
    
#     def peek(self):
#         return self.expression[len(self.expression)-1]
    
#     def size(self):
#         return len(self.expression)
    
#     def bracket_verifier(self):
#         temp_stack = [] 
        
#         while not self.isEmpty():
#             character = self.pop()
#             if character == ")":
#                 temp_stack.append(")")
#             elif character == "(":
#                 if len(temp_stack) == 0:
#                     return "Inválida"
#                 temp_stack.pop()
        
#         if len(temp_stack) == 0:
#             return "Válida"
#         else:
#             return "Inválida"
        
# expressao = Stack()
# texto = "(2 + 3) * (5 - 1)"

# for caractere in texto:
#     expressao.push(caractere)

# resultado = expressao.bracket_verifier()
# print(resultado)

# 3

# class Stack():

#     def __init__(self):
#         self.actions = []

#     def isEmpty(self):
#         return self.actions == []
    
#     def push(self, item):
#         return self.actions.append(item)
    
#     def pop(self):
#         return self.actions.pop()
    
#     def peek(self):
#         return self.actions[len(self.actions)-1]
    
#     def size(self):
#         return len(self.actions)
    
#     def undoAction(self):
#         undone = self.actions.pop()
#         return print(f"Ação desfeita: {undone}")
    
#     def showActions(self):
#         for action in self.actions:
#             print(action)

# photoshop = Stack()
# photoshop.push("Digitou: Olá")
# photoshop.push("Digitou: mundo")
# photoshop.push("Alterou fonte")
# photoshop.undoAction()

# print("\nAções restantes: ")
# photoshop.showActions()

# 4

