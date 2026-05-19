# import random

# # # Bubble Sort

# def bubble_sort(lista):

#     tamanho = len(lista)

#     #controlar quantas passagens foram feitas (repetições do sort)
#     passagem = 0

#     #enquanto ainda existirem passagens necessárias
#     while passagem < tamanho - 1:

#         print(f"\n======= PASSAGEM {passagem + 1} =======")

#         # indice para percorrer a lista
#         i = 0

#         # percorre apenas a parte ainda não ordenada
#         while i < tamanho - 1 - passagem:

#             print(f"Comparando {lista[i]} e {lista[i+1]}")

#             #se o elemento atual for maior que o próximo
#             #eles estão na ordem errada
#             if lista[i] > lista[i+1]:
#                 print("Troca realizada")

#                 #troca dos elementos
#                 aux = lista[i]
#                 lista[i] = lista[i+1]
#                 lista[i+1] = aux
#             else:
#                 print("Nenhuma troca necessária")
            
#             #mostra o estado atual da lista
#             print("Lista atual", lista)

#             #avança para o próxima elemento
#             i += 1

#         #finaliza uma passagem completa
#         passagem += 1

#     return lista

# numeros = [8, 3, 7, 1, 5, 2]

# def bubble_sort_resumido(lista):
#     tamanho = len(lista)
#     passagem = 0

#     while passagem < tamanho - 1:
#         i = 0

#         while i < tamanho - 1:
#             if lista[i] > lista[i+1]:
#                 aux = lista[i]
#                 lista[i] = lista[i+1]
#                 lista[i+1] = aux
#             i += 1
#         passagem += 1
#     return lista

# numeros = []

# for i in range(10000):
#     numeros.append(random.randint(1, 10000))

# print("Lista original: ", numeros)
# resultado = bubble_sort_resumido(numeros)
# print("Lista ordenada", resultado)

# Selection Sort

# def selection_sort(lista):

#     #tamanho da lista
#     tamanho = len(lista)

#     #índice da posição atual da ordenação
#     atual = 0

#     while atual < tamanho - 1:
#         print(f"======= PASSAGEM {atual + 1} =======")

#         # assume inicialmente que o menor elemento
#         # está na posição atual
#         indice_menor = atual

#         # indice usado para procurar o menor valor
#         i = atual + 1

#         #procura o menor elemento restante da lista
#         while i < tamanho:
#             print(f"Comparando {lista[i]} com {lista[indice_menor]}")

#             # se encontrar um valor menor, atualiza o índice do menor elemento
#             if lista[i] < lista[indice_menor]:
#                 print(f"{lista[i]} é o novo menor valor")
#                 indice_menor = i

#             #avança para o próximo elemento
#             i += 1
        
#         #após encontrar o menor elemento
#         #realiza a troca
#         if indice_menor != atual:
#             print(f"Troca {lista[atual]} por {lista[indice_menor]}")

#             aux = lista[atual]
#             lista[atual] = lista[indice_menor]
#             lista[indice_menor] = aux
#         else:
#             print("Nenhuma troca realizada")

#         print("Lista atual: ", lista)

#         #avança para a próxima posição
#         atual += 1

#     return lista

# numeros = [8, 3, 7, 1, 2]

# print("Lista original: ", numeros)
# resultado = selection_sort(numeros)
# print("Lista ordenada", resultado)

# def selection_sort_resumido(lista):
#     tamanho = len(lista)
#     atual = 0

#     while atual < tamanho - 1:
#         indice_menor = atual
#         i = atual + 1

#         while i < tamanho:
#             if lista[i] < lista[indice_menor]:
#                 indice_menor = i

#             i += 1
        
#         if indice_menor != atual:
#             aux = lista[atual]
#             lista[atual] = lista[indice_menor]
#             lista[indice_menor] = aux

#         atual += 1

#     return lista

# numeros = [8, 3, 7, 1, 2]

# print("Lista original: ", numeros)
# resultado = selection_sort(numeros)
# print("Lista ordenada", resultado)

# Insertion Sort

def insertion_sort(lista):
    # começamos do índice 1, pois o primeiro elemento sozinho
    # já pode ser considerado ordenado.
    i = 1

    #percorre a lista
    while i < len(lista):
        print(f"\n======== PASSAGEM {i} ========")

        #elemento atual que será inserido
        valor_atual = lista[i]

        print(f"Valor escolhido: {valor_atual}")

        #indice da posição anterior
        j = i - 1

        #enquanto existir um elemento anterior e o elemento anterior
        #for maior
        while j >= 0 and lista[j] > valor_atual:
            print(f"{lista[j]} é maior que {valor_atual}")
            print(f"Movendo {lista[j]} para a direita.")

            #move o elemento maior uma posição para frente
            lista[j+1] = lista[j]

            #volta uma posição
            j -= 1
            print("Estado atual", lista)
        
        lista[j+1] = valor_atual
        print(f"Inserindo {valor_atual} na posição correta")
        print("Lista após a inserção", lista)

        i += 1

    return lista

def insertion_sort_resumido(lista):
    i = 1

    while i < len(lista):
        valor_atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_atual:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valor_atual
        i += 1

    return lista

numeros = [8, 3, 7, 1, 5, 2]
print("Lista original: ", numeros)
resultado = insertion_sort_resumido(numeros)
print("Resultado: ", numeros)