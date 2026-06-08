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
#         print(f"Ação desfeita: {undone}")
#         return
    
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

# class Queue():

#     def __init__(self):
#         self.fila = []

#     def isEmpty(self):
#         return self.fila == []
    
#     def enqueue(self, item):
#         return self.fila.insert(0, item)
    
#     def dequeue(self):
#         return self.fila.pop()
    
#     def size(self):
#         return len(self.fila)
    
#     def show(self):
#         for i, item in enumerate(self.fila):
#             if i == 0:
#                 print(item, end=" ")
#             else:
#                 print(f"-> {item}", end=" ")

# filaMedica = Queue()

# filaMedica.enqueue("Ana")
# filaMedica.enqueue("Carlos")
# filaMedica.enqueue("Marina")

# print("Fila atual:\n")
# filaMedica.show()

# print(f"\ncliente atendido: {filaMedica.dequeue()}")

# print("Fila atual:\n")
# filaMedica.show()

# 5

# class Documento():

#     def __init__(self, nome:str, usuario:str, paginas:int):
#         self.nome = nome
#         self.usuario = usuario
#         self.paginas = paginas

# class Queue():

#     def __init__(self):
#         self.documentos = []

#     def isEmpty(self):
#         return self.documentos == []
    
#     def enqueue(self, item):
#         return self.documentos.insert(0, item)
    
#     def dequeue(self):
#         return self.documentos.pop()
    
#     def size(self):
#         return len(self.documentos)
    
#     def show(self):
#         for i, item in enumerate(self.documentos):
#             if i == 0:
#                 print(item, end=" ")
#             else:
#                 print(f"-> {item}", end=" ")

#     def printingQueue(self):
#         for documento in self.documentos[::-1]:
#             print(f"Documento: {documento.nome}\nUsuário: {documento.usuario}\nPáginas: {documento.paginas}\n")

#     def nextPrinting(self):
#         documento = self.dequeue()
#         print(f"Imprimindo: {documento.nome}\nUsuário: {documento.usuario}\nPáginas: {documento.paginas}\n")

# doc1 = Documento("prova.pdf", "Professor", 4)
# doc2 = Documento("trabalho.docx", "Aluno", 8)

# arquivos = Queue()
# arquivos.enqueue(doc1)
# arquivos.enqueue(doc2)

# arquivos.printingQueue()

# arquivos.nextPrinting()

# 6

# class Pedido():

#     def __init__(self, codigo:int, cliente:str, valor_total:float):
#         self.codigo = codigo
#         self.cliente = cliente
#         self.valor_total = valor_total        

# class Queue():

#     def __init__(self):
#         self.pedidos = []

#     def isEmpty(self):
#         return self.pedidos == []
    
#     def enqueue(self, item):
#         return self.pedidos.insert(0, item)
    
#     def dequeue(self):
#         return self.pedidos.pop()
    
#     def size(self):
#         return len(self.pedidos)
    
#     def show(self):
#         for i, item in enumerate(self.pedidos):
#             if i == 0:
#                 print(item, end=" ")
#             else:
#                 print(f"-> {item}", end=" ")

#     def orderQueue(self):
#         print("\nPedidos Atuais:")
#         for pedido in self.pedidos[::-1]:
#             print(f"Código: {pedido.codigo}\nCliente: {pedido.cliente}\nValor Total: {pedido.valor_total}\n")

#     def nextOrder(self):
#         pedido = self.dequeue()
#         print(f"Pedido Processado: {pedido.codigo}\nCliente: {pedido.cliente}\nValor Total: {pedido.valor_total}\nPedidos pendentes: {self.size()}")

# pedido1 = Pedido(101, "Lucas", 250.00)
# pedido2 = Pedido(102, "Bianca", 120.50)

# ecommerce = Queue()
# ecommerce.enqueue(pedido1)
# ecommerce.enqueue(pedido2)

# ecommerce.orderQueue()

# ecommerce.nextOrder()

# ecommerce.orderQueue()

# 7

# def organizarNotas(notas):
#     tamanho = len(notas)
#     passagem = 0
#     x = 0

#     while passagem < tamanho - 1:
#         i = 0

#         while i < tamanho - 1 - passagem:
#             if notas[i] > notas[i+1]:
#                 aux = notas[i]
#                 notas[i] = notas[i+1]
#                 notas[i+1] = aux

#             i += 1
#         x += 1
#         passagem += 1

#     print("Notas ordenadas: ")
#     for nota in notas:
#         print(nota, end=", ")
#     print(f"\nQuantidade de trocas: {x}")
#     return notas

# notas = [7.5, 5.0, 9.0, 6.5, 8.0]

# organizarNotas(notas)

# 8

# class Jogador():

#     def __init__(self, nome:str, pontuacao:int):
#         self.nome = nome
#         self.pontuacao = pontuacao

#     def __repr__(self):
#         return f"{self.nome}: {self.pontuacao}"
    
# def ordenarPontuacao(lista):
#     tamanho = len(lista)
#     atual = 0

#     while atual < tamanho - 1:
#         indice_menor = atual
#         i = atual + 1

#         while i < tamanho:
#             if lista[i].pontuacao > lista[indice_menor].pontuacao:
#                 indice_menor = i

#             i += 1

#         if indice_menor != atual:
#             aux = lista[atual]
#             lista[atual] = lista[indice_menor]
#             lista[indice_menor] = aux

#         atual += 1
    
#     print("Ranking:")
#     for i, jogador in enumerate(lista):
#         print(f"{i+1}º Lugar: {jogador.nome} - {jogador.pontuacao}")

#     return lista

# jogador1 = Jogador("Ana", 120)
# jogador2 = Jogador("Carlos", 90)
# jogador3 = Jogador("Marina", 150)
# jogador4 = Jogador("João", 110)

# jogadores = [jogador1, jogador2, jogador3, jogador4]

# ordenarPontuacao(jogadores)

# 9

# def recursiveSum(numeros):
#     if len(numeros) == 0:
#         return 0
    
#     return numeros[0] + recursiveSum(numeros[1:])

# valores = [35.90, 12.50, 8.00, 20.0]

# print(f"Total da compra: R${recursiveSum(valores)}")

# 10

# def contagemRegressiva(n):
#     if n <= 0:
#         return 0
    
#     print(n)
#     contagemRegressiva(n - 1)

# print("Contagem regressiva de 5: ")
# contagemRegressiva(5)
# print("Lançar!")

# 11

# class Produto():

#     def __init__(self, codigo:int, nome:str, preco:float):
#         self.codigo = codigo
#         self.nome = nome
#         self.preco = preco

# def buscarProduto(lista, alvo):
#     i = 0

#     while i < len(lista):
#         if lista[i].codigo == alvo:
#             return f"Produto encontrado:\nCódigo: {alvo}\nNome: {lista[i].nome}\nPreço: R${lista[i].preco}"
        
#         i += 1
        
#     return "Item não encontrado no estoque!"

# produto1 = Produto(101, "Arroz", 25.90)
# produto2 = Produto(205, "Feijão", 8.50)
# produto3 = Produto(150, "Macarrão", 5.75)
# produtos = [produto1, produto2, produto3]

# print(buscarProduto(produtos, 205))

# 12

# class Aluno():

#     def __init__(self, ra:int, nome:str):
#         self.ra = ra
#         self.nome = nome

# def buscaBinaria(lista, alvo, inicio, fim):
#     if inicio > fim:
#         return -1
    
#     meio = (inicio + fim) // 2

#     if lista[meio].ra == alvo:
#         print(f"Aluno encontrado:\nRA: {lista[meio].ra}\nNome: {lista[meio].nome}")
#         return
    
#     if alvo < lista[meio].ra:
#         return buscaBinaria(lista, alvo, inicio, meio - 1)
    
#     return buscaBinaria(lista, alvo, meio + 1, fim)

# aluno1 = Aluno(2024001, "Ana")
# aluno2 = Aluno(2024002, "Bruno")
# aluno3 = Aluno(2024003, "Carla")
# aluno4 = Aluno(2024004, "Daniel")
# aluno5 = Aluno(2024005, "Eduarda")
# alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

# buscaBinaria(alunos, 2024004, 0, len(alunos)-1)

# 13

# class Produto():

#     def __init__(self, codigo:int, nome:str, preco:float):
#         self.codigo = codigo
#         self.nome = nome
#         self.preco = preco

# def buscaBinaria(alvo, lista, inicio, fim):
#     if inicio > fim:
#         return -1
    
#     meio = (inicio + fim) // 2

#     if lista[meio].codigo == alvo:
#         print(f"\nProduto encontrado:\nCódigo: {lista[meio].codigo}\nNome: {lista[meio].nome}\nPreço: R${lista[meio].preco}")
#          return
    
#     if alvo < lista[meio].codigo:
#         return buscaBinaria(alvo, lista, inicio, meio - 1)
    
#     return buscaBinaria(alvo, lista, meio + 1, fim)

# def buscaCompleta(alvo, lista):
#     tamanho = len(lista)
#     atual = 0

#     while atual < tamanho - 1:
#         indice_menor = atual
#         i = atual + 1

#         while i < tamanho:

#             if lista[i].codigo < lista[indice_menor].codigo:
#                 indice_menor = i

#             i += 1

#         if indice_menor != atual:
#             aux = lista[atual]
#             lista[atual] = lista[indice_menor]
#             lista[indice_menor] = aux

#         atual += 1

#     print("Produtos ordenados por código:\n")
#     for produto in lista:
#         print(f"{produto.codigo} - {produto.nome} - R${produto.preco}")

#     return buscaBinaria(alvo, lista, 0, len(lista) - 1)

# produto1 = Produto(305, "Teclado", 120.00)
# produto2 = Produto(101, "Mouse", 59.90)
# produto3 = Produto(450, "Monitor", 899.00)
# produto4 = Produto(220, "Webcam", 199.90)
# produto5 = Produto(150, "Headset", 249.90)
# produtos = [produto1, produto2, produto3, produto4, produto5]

# buscaCompleta(220, produtos)

# 14

# class Arquivo():

#     def __init__(self, nome:str, tamanho_mb:int):
#         self.nome = nome
#         self.tamanho_mb = tamanho_mb

# class Pasta():

#     def __init__(self, nome:str):
#         self.nome = nome
#         self.itens = []

#     def adicionar(self, item):
#         self.itens.append(item)

# def calcularMb(p):
#     total = 0

#     if isinstance(p, Arquivo):
#         if p.tamanho_mb <= 0:
#             return 0
#         return p.tamanho_mb
    
#     if isinstance(p, Pasta):
#         for item in p.itens:
#             total += calcularMb(item)

#     return total

# arquivo1 = Arquivo("main.py", 2)
# arquivo2 = Arquivo("README.md", 1)

# imagem1 = Arquivo("logo.png", 5)
# imagem2 = Arquivo("banner.png", 8)

# documento1 = Arquivo("contrato.pdf", 12)

# nota1 = Arquivo("anotacoes.txt", 3)

# pasta_imagens = Pasta("imagens")
# pasta_imagens.adicionar(imagem1)
# pasta_imagens.adicionar(imagem2)

# pasta_notas = Pasta("notas")
# pasta_notas.adicionar(nota1)

# pasta_documentos = Pasta("documentos")
# pasta_documentos.adicionar(documento1)
# pasta_documentos.adicionar(pasta_notas)

# pasta_projeto = Pasta("Projeto")
# pasta_projeto.adicionar(arquivo1)
# pasta_projeto.adicionar(arquivo2)
# pasta_projeto.adicionar(pasta_imagens)
# pasta_projeto.adicionar(pasta_documentos)

# print(f"O tamanho total em MB é: {calcularMb(pasta_projeto)}")

#Pergunta 1: A recursão vai reiniciar caso o arquivo não possua nenhum mb.
#Pergunta 2: Ao somar a própria recursão ao total com o item atual. Isso irá continuar a recursão até todos os arquivos serem somados.
#Pergunta 3: Pois estamos precisamos calcular valores internos, entrando cada vez mais nos arquivos e dividindo o problema em partes menores.
#Pergunta 4: O sistema entraria em loop infinito, pois iria tentar ler a própria pasta sem parar.
#Pergunta 5: O total de arquivos também existira começando por 0. E a cada mb e arquivo, inserimos na recursão.

# 15 - Desafio Integrador

class Cliente():

    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf

class Servico():
    def __init__(self, codigo:int, descricao:str, valor:float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

class Atendimento():
    def __init__(self, cliente:str):
        self.cliente = cliente
        self.servicos = []
        self.status = ""

class Stack():

    def __init__(self):
        self.actions = []

    def isEmpty(self):
        return self.actions == []

    def push(self, action):
        self.actions.append(action)
    
    def pop(self):
        return self.actions.pop()
    
    def peek(self):
        return self.actions[len(self.actions)-1]
    
    def size(self):
        return len(self.actions)
    
    def show(self):
        print("\nHistórico de Ações:")
        for action in self.actions:
            print(action, end="\n\n")

historico = Stack()
servico1 = Servico(301, "Formatação", 120.00)
servico2 = Servico(105, "Limpeza interna", 80.00)
servico3 = Servico(220, "Troca de teclado", 150.00)
servico4 = Servico(410, "Instalação de SSD", 250.00)
servico5 = Servico(180, "Diagnóstico", 50.00)
servicos_disponiveis = [servico1, servico2, servico3, servico4, servico5]

class Queue():

    def __init__(self):
        self.fila = []
        self.atendimentoAtual = None

    def isEmpty(self):
        return self.fila == []
    
    def enqueue(self, item):
        self.fila.insert(0, item)
        print(f"O cliente {item.cliente.nome} entrou na fila")
        historico.push(f"O cliente {item.cliente.nome} entrou na fila")
    
    def dequeue(self):
        return self.fila.pop()
    
    def size(self):
        return len(self.fila)
    
    def show(self):
        for item in self.fila:
            if self.fila[0] == item:
                print(item, end=" ")
            else:
                print(f"{item} ->", end=" ")
    
    def iniciarAtendimento(self):
        self.atendimentoAtual = self.dequeue()
        self.atendimentoAtual.status = "Em atendimento"
        print(f"\nAtendimento iniciado:\n{self.atendimentoAtual.cliente.nome}\nStatus: {self.atendimentoAtual.status}")
        historico.push(f"O cliente {self.atendimentoAtual.cliente.nome} entrou em atendimento.")
        
        return self.atendimentoAtual
    
    def finalizarAtendimento(self):
        if self.atendimentoAtual == None:
            print("Nenhum atendimento em andamento.")
            return
        
        self.atendimentoAtual.status = "Finalizado"
        print(f"\nAtendimento finalizado:\nCliente: {self.atendimentoAtual.cliente.nome}\nCPF: {self.atendimentoAtual.cliente.cpf}\nStatus: {self.atendimentoAtual.status}")
        historico.push(f"O atendimento de {self.atendimentoAtual.cliente.nome} foi finalizado.")
        self.atendimentoAtual = None
        
        return self.atendimentoAtual

    def buscarServicoSequencial(self, alvo):
        i = 0
        
        if self.atendimentoAtual == None:
            print("Ninguém está sendo atendido no momento.")
            return
        
        while i < len(servicos_disponiveis):
            if servicos_disponiveis[i].codigo == alvo:
                print(f"\nServiço encontrado:\nCódigo: {servicos_disponiveis[i].codigo}\nDescrição: {servicos_disponiveis[i].descricao}\nPreço: {servicos_disponiveis[i].valor}")
                adicao = str(input("Você deseja adicionar o serviço ao atendimento atual? (S/N): "))
                if adicao == "s" or adicao == "S":
                    self.atendimentoAtual.servicos.append(servicos_disponiveis[i])
                    print(f"\nServiço adicionado ao atendimento de {self.atendimentoAtual.cliente.nome}:\n{servicos_disponiveis[i].descricao}")
                    historico.push(f"O cliente {self.atendimentoAtual.cliente.nome} registrou o seguinte serviço:\n{servicos_disponiveis[i].descricao}")
                    return
                else:
                    print("O serviço foi encontrado.")
                    return
        
            i += 1

        print("Serviço não encontrado.")
        return
    
    def ordernarServicos(self, servicos):
        tamanho = len(servicos)
        passagem = 0

        while passagem < tamanho - 1:
            i = 0

            while i < tamanho - 1:
                if servicos[i].codigo > servicos[i+1].codigo:
                    aux = servicos[i]
                    servicos[i] = servicos[i+1]
                    servicos[i+1] = aux

                i += 1
            passagem += 1

        print("\nServiços ordenados por código:")
        for servico in servicos:
            print(f"{servico.codigo} - {servico.descricao} - {servico.valor}")
        return servicos
            
    def buscarServicoBinario(self, alvo):
        if self.atendimentoAtual == None:
            print("Ninguém está sendo atendido no momento.")
            return
        
        self.ordernarServicos(servicos_disponiveis)
        
        def executarBuscaBinaria(lista, inicio, fim):
            if inicio > fim:
                return None
            
            meio = (inicio + fim) // 2
            
            if lista[meio].codigo == alvo:
                return lista[meio]
            
            if lista[meio].codigo > alvo:
                return executarBuscaBinaria(lista, inicio, meio - 1)
            else:
                return executarBuscaBinaria(lista, meio + 1, fim)
            
        resultado = executarBuscaBinaria(servicos_disponiveis, 0, len(servicos_disponiveis)-1)
        
        if resultado is not None:
            print(f"\nServiço encontrado:\nCódigo: {resultado.codigo}\nDescrição: {resultado.descricao}\nPreço: {resultado.valor}")
            adicao = str(input("Você deseja adicionar o serviço ao atendimento atual? (S/N): "))
            if adicao == "s" or adicao == "S":
                self.atendimentoAtual.servicos.append(resultado)
                print(f"\nServiço adicionado ao atendimento de {self.atendimentoAtual.cliente.nome}:\n{resultado.descricao}")
                historico.push(f"O cliente {self.atendimentoAtual.cliente.nome} registrou o seguinte serviço:\n{resultado.descricao}")
            else:
                print("O serviço foi encontrado.")
                return
        else:
            print("Serviço não encontrado.")
            return
        
    def calcularTotalAtendimento(self, atendimento, i = 0):
        if i == len(atendimento.servicos):
            return 0
        
        return atendimento.servicos[i].valor + self.calcularTotalAtendimento(atendimento, i + 1)
    
valdirgames = Queue()

cliente1 = Cliente("Ana", "111")
cliente2 = Cliente("Bruno", "222")
atendimento1 = Atendimento(cliente1)
atendimento2 = Atendimento(cliente2)
valdirgames.enqueue(atendimento1)
valdirgames.enqueue(atendimento2)

valdirgames.iniciarAtendimento()

valdirgames.buscarServicoSequencial(220)
valdirgames.buscarServicoBinario(180)

print(f"\nTotal do atendimento: R${valdirgames.calcularTotalAtendimento(atendimento1)}")

valdirgames.finalizarAtendimento()

historico.show()

print(f"\nÚltima ação desfeita: {historico.pop()}")