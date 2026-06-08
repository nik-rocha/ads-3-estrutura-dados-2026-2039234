# def somar_recursivo(numeros):
#     if len(numeros) == 0:
#         return 0

#     return numeros[0] + somar_recursivo(numeros[1:])

# def contar(itens):
#     if itens == []:
#         return 0
    
#     return 1 + contar(itens[1:])

# pessoas = ["Ana", "Bruno", "Caio"]
# resultado = contar(pessoas)
# print(resultado)

# Busca Sequencial

# def busca_sequencial(lista, alvo):
#     indice = 0
    
#     while indice < len(lista):
#         if lista[indice] == alvo:
#             return indice
        
#         indice += 1
        
#     return -1

# Busca Binária

# def busca_binaria(lista, alvo, inicio, fim):
#     if inicio > fim:
#         return -1

#     meio = (inicio + fim) // 2

#     if lista[meio] == alvo:
#         return meio

#     if alvo < lista[meio]:
#         return busca_binaria(lista, alvo, inicio, meio - 1)

#     return busca_binaria(lista, alvo, meio + 1, fim)

# Exercícios Sugeridos

# def busca_sequencial(lista, alvo):
#     indice = 0
    
#     while indice < len(lista):
#         if lista[indice] == alvo:
#             return indice
        
#         indice += 1
        
#     return -1

# nomes = ["Jonas", "Miguel", "Eduardo", "Rogério", "Jefferson", "Jonas"]
# resultado = busca_sequencial(nomes, "Jefferson")
# print("Índice do nome:", resultado)

def busca_binaria(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == alvo:
        return meio
    
    if alvo < lista[meio]:
        return busca_binaria(lista, alvo, inicio, meio - 1)
    
    return busca_binaria(lista, alvo, meio + 1, fim)

notas = [4, 6.7, 8, 9.5, 10]
resultado = busca_binaria(notas, 9.5, 0, len(notas)-1)
print("Índice encontrado:", resultado)