class Jogador:
    
    def __init__(self, nametag:str, pontuacao:int):
        self.nametag = nametag
        self.pontuacao = pontuacao

class Scoreboard:
    
    def __init__(self, nomeEquipe:str):
        self.nomeEquipe = nomeEquipe
        self.score = {}
        
    def add_jogador(self, nomeJogador, pointJogador):
        self.score[nomeJogador] = pointJogador
        
    def update_pontos(self, nomeJogador, pointJogador):
        if nomeJogador in self.score:
            old_pontos = self.score[nomeJogador]
            self.score[nomeJogador] = pointJogador
            print(f"O jogador {nomeJogador} teve os pontos atualizados de {old_pontos} para {pointJogador}") 
        else:
            print(f"O jogador {nomeJogador} não existe")
            
    def verificar_pontos(self, nomeJogador):
        if nomeJogador in self.score:
            print(f"O jogador {nomeJogador} possui {self.score[nomeJogador]} pontos") 
        else:
            print(f"O jogador {nomeJogador} não existe")
            
    def list_jogadores(self):
        for jogador in self.score:
            print(f"Nametag: {jogador}. Pontos: {self.score[jogador]}")
            
    def maior_jogador(self):
        maior = 0
        nome_maior = None
        
        for jogador in self.score:
            if self.score[jogador] > maior:
                maior = self.score[jogador]
                nome_maior = jogador
                
        print(f"O jogador {nome_maior} tem a maior quantidade de pontos, estando com {maior} pontos.")
        
    def ordenar_ranking(self):
        mostrados = {}
        posicao = 1

        while len(mostrados) < len(self.score):
            maior = -1
            jogador_maior = None
            
            for jogador in self.score:
                if jogador not in mostrados:
                    if self.score[jogador] > maior:
                        maior = self.score[jogador]
                        jogador_maior = jogador
                        
            print(f"{posicao}º = {jogador_maior} : {maior} pontos")
            mostrados[jogador_maior] = maior
            posicao += 1
    
teamAlpha = Scoreboard("Team Alpha")

jeff = Jogador("Mr. Jeff", 10)
johnes = Jogador("Mr. Johnes", 20)

teamAlpha.add_jogador(jeff.nametag, jeff.pontuacao)
teamAlpha.add_jogador(johnes.nametag, johnes.pontuacao)

teamAlpha.list_jogadores()
teamAlpha.maior_jogador()

teamAlpha.ordenar_ranking()