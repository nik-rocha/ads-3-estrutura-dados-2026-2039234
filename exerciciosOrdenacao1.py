#-------------------------------------------- Ex. 1

def bubble_sort_decrescente(lista):
    tamanho = len(lista)
    passagem = 0

    while passagem < tamanho - 1:
        i = 0

        while i < tamanho - 1:
            # diferente de um bubble padrão, é só verificar se o
            # índice é menor ao invés de maior do que o próximo item
            if lista[i] < lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            i += 1
        passagem += 1

    return lista

numeros = [15, 2, 30, 9, 1]

print(numeros)
resultado = bubble_sort_decrescente(numeros)
print(resultado)

#-------------------------------------------- Ex. 2

def selection_sort_decrescente(lista):
    tamanho = len(lista)
    atual = 0

    while atual < tamanho - 1:
        indice_maior = atual
        i = atual + 1

        while i < tamanho:
            # diferente de um selection padrão, é só verificar se o
            # índice é maior do que o MAIOR existente
            if lista[i] > lista[indice_maior]:
                indice_maior = i

            i += 1

        if indice_maior != atual:
            aux = lista[atual]
            lista[atual] = lista[indice_maior]
            lista[indice_maior] = aux

        atual += 1
    
    return lista

numeros = [120, 450, 200, 980, 300]

print("Lista original: ", numeros)
resultado = selection_sort_decrescente(numeros)
print("Lista ordenada", resultado)

#-------------------------------------------- Ex. 3

def bubble_sort_letras(lista):
    tamanho = len(lista)
    passagem = 0

    while passagem < tamanho - 1:
        i = 0

        while i < tamanho - 1:
            #como ainda estamos falando de números, é só usar o valor
            #numérico da quantidade de letras de cada item

            #extra: se o tamanho das palavras for o mesmo, ele segue
            #procedimento padrão, pois isso fará o sort
            #alfabeticamente.
            if len(lista[i]) == len(lista[i+1]):
                if lista[i] > lista[i+1]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux

                i += 1
            else:
                if len(lista[i]) > len(lista[i+1]):
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux

                i += 1

        passagem += 1

    return lista

palavras = ["python", "ia", "estrutura", "ai", "web", "dados"]

print(palavras)
resultado = bubble_sort_letras(palavras)
print(resultado)