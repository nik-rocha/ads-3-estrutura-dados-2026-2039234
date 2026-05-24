class Produto:

    def __init__(self, nome:str, preco:int, categoria:str):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Loja:
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, produto):
        self.produtos.remove(produto)

    def ordenarProdutos(self):
        ordenacao = str(input("\nQual ordenação você deseja realizar?\n C = Crescente, D = Decrescente: "))

        if ordenacao == "C" or ordenacao == "c":
            tamanho = len(self.produtos)
            passagem = 0

            while passagem < tamanho - 1:
                i = 0

                while i < tamanho - 1 - passagem:

                    if self.produtos[i].preco > self.produtos[i+1].preco:
                        aux = self.produtos[i].preco
                        self.produtos[i].preco = self.produtos[i+1].preco
                        self.produtos[i+1].preco = aux

                    i += 1
                passagem += 1

            print("\nProdutos atuais em ordem crescente:")
            for produto in self.produtos:
                print(f"{produto.categoria} - {produto.nome}: R${produto.preco}")
            return self.produtos
        else:
            tamanho = len(self.produtos)
            passagem = 0

            while passagem < tamanho - 1:
                i = 0

                while i < tamanho - 1 - passagem:

                    if self.produtos[i].preco < self.produtos[i+1].preco:
                        aux = self.produtos[i].preco
                        self.produtos[i].preco = self.produtos[i+1].preco
                        self.produtos[i+1].preco = aux

                    i += 1
                passagem += 1

            print("\nProdutos atuais em ordem decrescente:")
            for produto in self.produtos:
                print(f"{produto.categoria} - {produto.nome}: R${produto.preco}")
            return self.produtos
        
    def mostrarProdutos(self):
        print("\nProdutos atuais:")
        for produto in self.produtos:
            print(f"{produto.categoria} - {produto.nome}: R${produto.preco}")
        
    
notebook = Produto("Notebook", 3500, "Eletrônicos")
mouse = Produto("Mouse", 120, "Periféricos")
teclado = Produto("Teclado", 250, "Periféricos")
monitor = Produto("Monitor", 900, "Acessórios")

loja = Loja()

loja.adicionarProduto(notebook)
loja.adicionarProduto(mouse)
loja.adicionarProduto(teclado)
loja.adicionarProduto(monitor)

loja.mostrarProdutos()
loja.ordenarProdutos()

# Questão 1: A vantagem é a organização dos itens, isso pode ser usado em casos de produtos reais aplicando a ordenação, deixando o projeto mais eficiente.

# Questão 2: Pois a forma como funciona, analisando cada item seguinte e invertendo suas ordens, começa a pesar bastante para sistemas com grande quantidade de dados.

# Questão 3: Foi usado apenas o preço.