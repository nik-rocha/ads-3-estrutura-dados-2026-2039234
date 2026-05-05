class Ranking:
    
    def __init__(self, nomeJogo:str):
        self.nomeJogo = nomeJogo
        self.ranking = []
        
    def adicionarJogador(self, j):
        if len(self.ranking) == 10:
            print("Você não pode adicionar mais de 10 jogadores.\n")
        else:
            self.ranking.append(j) 
        
    def adicionarJogadorOrdenado(self, i, j):
        if type(i) is str:
            print(f"O valor digitado não é um índice válido e o jogador não será adicionado. (Jogador: {j})\n")
        elif len(self.ranking) == 10:
            print("Você não pode adicionar mais de 10 jogadores.\n")
        else:
            self.ranking.insert(i, j)
        
    def removerJogador(self, i):
        if type(i) is str:
            print(f"O valor digitado não é um índice válido e nenhum jogador será removido. (Índice: {i})\n")
        else:
            del self.ranking[i]
        
    def ordenarJogadores(self):
        self.ranking.sort()
        
    def listarJogadores(self):
        for jogador in self.ranking:
            print(f"{jogador}")
        print("\n")
        
    def contadorDeJogadores(self, j):
        a = 0
        
        for jogador in self.ranking:
            if jogador == j:
                a += 1
            else:
                continue
        
        print(f"Existem {a} jogadores com o nome {j} em seu ranking.\n\n")
        
marioKart = Ranking("Mario Kart Wii")            
print("Bem vindo a Mario Kart Wii! Escolha o que você quer fazer com os jogadores: ")

while True:
    opcao = input("[A] = Adicionar jogador\n[AO] = Adicionar jogador ordenado\n[R] = Remover jogador\n[O] = Ordenar jogadores\n[L] = Listar jogadores\n[C] = Contar jogadores com nomes iguais\n[0] = Parar\n")

    if opcao == "A" or opcao == "a":
        aask = int(input("Quantas vezes você quer adicionar?\n"))
        ax = 0
        
        while ax < aask:
            aname = str(input("Digite o nome do jogador: "))
            marioKart.adicionarJogador(aname)
            ax += 1
        continue
        

    elif opcao == "AO" or opcao == "ao":
        aoask = int(input("Quantas vezes você quer adicionar, em ordem?\n"))
        aox = 0
        
        while aox < aoask:
            aoi = int(input("Digite a posição do jogador: "))
            aoname = str(input("Digite o nome do jogador: "))
            marioKart.adicionarJogadorOrdenado(aoi, aoname)
            aox += 1
        continue
            
    elif opcao == "R" or opcao == "r":
        rask = int(input("Quantas vezes você quer remover o jogador, por posição?\n"))
        rx = 0
        
        while rx < rask:
            ri = int(input("Digite a posição do jogador: "))
            marioKart.removerJogador(ri)
            rx += 1
        continue
            
    elif opcao == "O" or opcao == "o":
        marioKart.ordenarJogadores()
        print(f"Seu ranking agora é: {marioKart.listarJogadores()}\n")
        continue
        
    elif opcao == "L" or opcao == "l":
        print(f"Seu ranking: {marioKart.listarJogadores()}\n")
        continue
    
    elif opcao == "C" or opcao == "c":
        cx = 0
        cname = str(input("Digite o nome que você quer contar: \n"))
        
        marioKart.contadorDeJogadores(cname)
        continue
    
    elif opcao == "0":
        print("Fechando o jogo...")
        break
    
    else:
        print("Opção inválida! Tente novamente")
        continue
        