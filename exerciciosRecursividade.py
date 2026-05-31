# 1

# def fibonacci(n):
#     if n <= 1:
#         return n
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(f"Posição encontrada: {fibonacci(5)}")

# 2

# def fatorial(n):
#     if n <= 1:
#         return n
    
#     return n * fatorial(n-1)

# print(f"Fatorial de 8: {fatorial(4)}")

# 3

# def somar_lista(lista):
#     if len(lista) == 0:
#         return 0
    
#     return lista[0] + somar_lista(lista[1:])

# numeros = [10, 20, 30, 40]
# print(f"Resultado da Soma: {somar_lista(numeros)}")

# 4

# def contagem_regressiva(n):
#     if n < 0:
#         return n
    
#     print(n)
#     contagem_regressiva(n - 1)

# print("Contagem regressiva!")
# contagem_regressiva(5)

# 5

# def listar_arquivos(lista):
#     x = 0

#     for item in lista:

#         if isinstance(item, list):
#             x += listar_arquivos(item)
#         else:
#             x += 1

#     return x

# estrutura = [
#     "foto.png",
#     "documento.pdf",
#     [
#         "vídeo.mp4",
#         [
#             "planilha.xlsx"
#         ]
#     ]
# ]

# total = listar_arquivos(estrutura)
# print(f"Total de arquivos: {total}")

# 6

def eh_palindromo(texto):
    texto = texto.lower()
    
    if len(texto) <= 1:
        return True
        
    if texto[0] != texto[-1]:
        return False
        
    return eh_palindromo(texto[1:-1])

print(eh_palindromo("arara"))

# Pergunta 1: O exercício 6.

# Pergunta 2: O exercício 2, pois me fez entender mais a funcionalidade, multiplicando o item por ele mesmo -1 com a função.

# Pergunta 3: O caso base vai definir qual situação a recursão vai chegar ao seu fim.

# Pergunta 4: Sem um caso base, a recursão nunca irá quebrar ou nunca parar.

# Pergunta 5: Problemas que exigem uma forma mais complexa de resolução. Como a recursão 

