# UNIMAR - Universidade de Marília

# Análise e Desenvolvimento de Sistemas

# 3º Termo - Turma C

# Nicollas Rocha - RA 2039234

# DESAFIO — O HISTÓRICO QUE NUNCA PARA
# Você foi contratado para desenvolver um sistema de histórico de navegação de uma plataforma
# educacional.
# O sistema deve registrar conteúdos acessados e permitir navegação entre eles.
# Regras:
# - Novos conteúdos são adicionados ao final.
# - É possível voltar e avançar no histórico.
# - Ao acessar um novo conteúdo após voltar, o futuro deve ser apagado.
# Seu desafio é implementar essa lógica utilizando uma estrutura de dados adequada.

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return f"{self.data}"

class HistoricoNavegacao:
    def __init__(self):
        self.head = None
        self.atual = None
        self.novo = False
    
    def registrar_acesso(self, node):
        newClass = Node(node)
        
        if self.head is None:
            self.head = newClass
            self.atual = newClass
            return newClass
        
        last = self.head
        
        while last.next is not None:
            last = last.next
            
        last.next = newClass
        self.atual = newClass
        
        self.novo = True
    
    def voltar(self):
        print("\nVoltando...")
        
        if self.head is None:
            return
        
        if self.atual == self.head:
            
            histReader = self.head
            
            while histReader.next is not None:
                histReader = histReader.next
                
            self.atual = histReader
            
            return
        
        histReader = self.head
        
        while histReader.next != self.atual:
            histReader = histReader.next
            
        self.atual = histReader
        
    def avancar(self):
        print("\nAvançando...")
        
        if self.head is None or self.atual == self.head:
            return
            
        if self.atual.next == None and self.novo == True:
            self.head = self.head.next
            self.novo = False
            self.atual = self.head

        elif self.atual.next == None and self.novo == False:
            self.atual = self.head
        else:
            self.atual = self.atual.next
            
    def contar_conteudos(self):
        self.novo = False
        
        i = 0
        count = self.head
        
        while count is not None:
            count = count.next
            i += 1
            
        return f"Você tem {i} conteúdos buscados."
    
    def buscar_conteudo(self, aula):
        self.novo = False
        
        count = self.head
        
        while count is not None:
            if count.data == aula:
                print(f"\nA aula '{aula}' foi encontrada no histórico.")
                return True
            
            count = count.next
            
        print(f"\nA aula '{aula}' NÃO foi encontrada no histórico.")
        return False
        
    def mostrar_historico(self): 
        print("\nHistórico Inicial:") 
    
        self.novo = False
    
        histReader = self.head
    
        while histReader is not None:
            if histReader == self.atual:
                print(f"-> {histReader} (ATUAL)")
            else:
                print(histReader)
            histReader = histReader.next
    
historico = HistoricoNavegacao()
historico.registrar_acesso("Aula 1 - Introdução")    
historico.registrar_acesso("Aula 2 - Variáveis")
historico.registrar_acesso("Aula 3 - Condicionais")
historico.registrar_acesso("Exercício 1")          
historico.mostrar_historico()
historico.avancar()
historico.mostrar_historico()
historico.registrar_acesso("Exercício 5")      
historico.avancar()
historico.mostrar_historico()
# historico.avancar()
# historico.mostrar_historico()
# historico.avancar()
# historico.mostrar_historico()
# historico.voltar()
# historico.mostrar_historico()
# historico.contar_conteudos()
# historico.buscar_conteudo("Aula 1 - Introdução")