## Dicionários

# Sistema de controle de estoque:
# - Cada produto deve ter nome e quantidade em estoque
# - O programa deve permitir:
#     - Adicionar produtos ao estoque
#     - Atualizar quantidade em estoque
#     - Consular quantidade de produto
#     - Listar todo o estoque

estoque = {
    "mouse": 10,
    "teclado": 5
} # {} Criam um dicionário

def add_produto(nome, quantidade):
    if nome not in estoque:
        estoque[nome] = quantidade
        return True
    else:
        print(f"Produto {nome} já existente na base, atualize o produto")
        return False
    
def show_produto(nome):
    if nome in estoque:
        print(f"Produto {nome} tem {estoque[nome]} itens em estoque")
    else:
        print("Produto não encontrado.")
        
def list_produto():
    print("Produtos em estoque:\n")
    for produto in estoque:
        print(f"{produto.capitalize()}: {estoque[produto]} em estoque")
        
def update_estoque(nome, quantidade):
    if nome in estoque:
        old_estoque = estoque[nome]
        estoque[nome] = quantidade
        print(f"Produto {nome} atualizado estoque de {old_estoque} para {quantidade}")
        
while True:
    print("\n1 - Adicionar produto")
    print("2 - Consultar produto")
    print("3 - Atualizar produto")
    print("4 - Listar estoque")
    print("0 - Sair\n")
        
    opcao = input("Escolha")
    
    if opcao == "1":
        nome = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        add_produto(nome, quantidade)
        
    if opcao == "2":
        nome = input("Produto: ")
        show_produto(nome)
        
    if opcao == "3":
        nome = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        update_estoque(nome, quantidade)
        
    if opcao == "4":
        list_produto()
        
    if opcao == "0":
        break