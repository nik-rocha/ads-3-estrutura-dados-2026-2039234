# # Crie um algoritmo que leia uma idade e verifique se é maior ou menor de idade

# idade = int(input("Informe sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Vocé é menor de idade")
    
# # Crie um algoritmo que leia N valores, quando for digitado 0, o algoritmo é encerrado e apresentado a soma e multiplicação de todos os valores digitados

# soma = 0
# mult = 1

# while True:
#     valor = int(input("Digita um valor (0 para encerrar):"))
    
#     if valor == 0:
#         break
    
#     soma += valor
#     mult *= valor
    
# print(f"A soma de todos os valores digitados é: {soma}")
# print(f"A multiplicação de todos os valores digitados é: {mult}")

# # Dado uma lista de inteiros, crie uma nova lista invertida usando loop (sem usar reverse) e função.

# l1 = [20, 30, 40, 50]


# def invercao(lista):
#     invertida = []    
#     print(f"Essa lista será invertida: {lista}.")

#     x = 0
#     indice = len(lista)

#     while x != len(lista):
#         indice -= 1
#         linvertida = lista[indice]
#         invertida.append(linvertida)
#         x += 1
    
#     return invertida
        
# l2 = invercao(l1)
# print(l2)

# nome = "Garibaldo"

# print(nome)
# print(nome.lower())
# print(nome.upper())

# print(nome[::-1].upper())

# for letra in nome:
#     print(letra)
    
# type(nome)

# print(nome[0:1])
# print(nome[0:2])
# print(nome[0:3])
# print(nome[::2])

# idades = [28, 20, 21, 25, 19, 30]

# print(type(idades))

# print(idades[::-1])
# print(idades[0:2])

# class Conta:
#     def __init__(self, titular:str, numero:str, saldo_inicial:float = 0.0):
#         self.titular = titular
#         self.numero = numero
#         self.saldo = saldo_inicial
    
#     def total(self):
#         return self.saldo
    
#     def saque(self, valor):
#         self.saldo -= valor
#         return self.saldo
        
#     def deposito(self, valor):
#         self.saldo += valor
#         return True
        
       
# conta1 = Conta("Maria dos Santos", "0001-1", 1000.0)
# print(type(conta1))

# # Exercício 1 - Dados Abstratos

# class Pessoa:
    
#     def __init__(self, nome:str, idade:int, cpf:str, altura:float, status:str = "Dormindo"):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf
#         self.altura = altura
#         self.status = status
        
#     def acordar(self, stat):
#         acorda = str(input("Você quer acordar? São 00:00 agora (S/N):"))
        
#         if acorda == "s" or acorda == "S":
#             h = 0
#             while h <= 8:
#                 print(f"São 0{h}:00 agora.")
#                 h += 1
#             print("Você acordou!")
#             self.status = stat
#             print(f"Seu status atual é '{self.status}' e você ganhou +1cm, estando agora com {self.altura + 0.01}.")
#         else:
#             print("Ok, você não acorda :)")
            
# pessoa1 = Pessoa("Jonas", 18, "133.133.133.13", 1.67)
# pessoa1.acordar("Acordado")
            
# # Exercício 2 - IMC

# class Pessoa:
    
#     def __init__(self, nome:str, idade:int, altura:float):
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura
        
#     def calcular_imc(self, peso):
#         imc = peso / (self.altura ** 2)
#         return imc
        
#     def faixas_imc(self, peso):
#         valorImc = self.calcular_imc(peso)
        
#         if valorImc < 18.5:
#             return f'Seu IMC é de {valorImc:.1f}. Você está abaixo da linha saudável'
#         elif valorImc > 18.5 and valorImc < 24.9:
#             return f'Seu IMC é de {valorImc:.1f}. Você está na normalidade.'
#         elif valorImc > 24.9 and valorImc < 29.9:
#             return f'Seu IMC é de {valorImc:.1f}. Você está com sobrepeso.'
#         elif valorImc > 29.9 and valorImc < 39.9:
#             return f'Seu IMC é de {valorImc:.1f}. Você está com obesidade.'
#         else:
#             return f'Seu IMC é de {valorImc:.1f}. Você está com obesidade severa.'

# pessoa1 = Pessoa('Eu, 2025', 18, 1.76)
# pessoa1.faixas_imc(110)

# Exercício 3 - Recorde de Vitórias

# l_size = int(input("Digite a quantidade de jogadas: "))
# l_size_counter = 0

# winner_list = []
# win_streak_list = []

# while l_size_counter < l_size:
#     winner_score = int(input("Digite os pontos de cada jogada respectivamente: "))
#     winner_list.append(winner_score)
#     l_size_counter += 1
    
# def calc_streak(list):
    
#     for w in list:
#         while w > 0:
#             win_streak_list.append(w)
#             return list

# calc_streak(winner_list)
# print(win_streak_list)

n = int(input())

i = 0
valores = list(map(int, input().split()))

print(valores)

i = 0
soma = 0
sequencia = 0
maior_soma = 0
maior_sequencia = 0

while i < len(valores):
    if valores[i] > 0:
        soma += valores[i]
        sequencia += 1

        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
            maior_soma = soma
    else:
        soma = 0
        sequencia = 0

    i += 1

print(maior_sequencia, maior_soma)
