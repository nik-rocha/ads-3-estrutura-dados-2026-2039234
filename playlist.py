class Musica:
    
    def __init__(self, nome:str, artista:str, duracaoMin:int, genero:str):
        self.nome = nome
        self.artista = artista
        self.duracaoMin = duracaoMin
        self.genero = genero
        
class Playlist:
    
    def __init__(self, nomePlaylist:str):
        self.nomePlaylist = nomePlaylist
        self.musicas = []
        
    def adicionarMusica(self, musica):
        self.musicas.append(musica)
        
    def removerMusica(self, musica):
        print(f"\n{musica.nome} - {musica.artista} foi removido. \n")
        self.musicas.remove(musica)
        
    def listarMusicas(self):
        print("\nSuas músicas são: \n")
        for musica in self.musicas:
            print(f"{musica.nome} - {musica.artista} - {musica.duracaoMin} minutos - {musica.genero}\n")
    
    def calculoTempo(self):
        tempo = 0
        
        for musica in self.musicas:
            tempo += musica.duracaoMin
            
        print("No total, você tem: \n")
        print(f"{tempo} minutos de música\n")
        
    def tempoPorG(self):
        generos = []
        tempoG = 0
        print("Por gênero, você tem: ")
        
        for musica in self.musicas:
            if musica.genero not in generos:
                generos.append(musica.genero)
                tempoG += musica.duracaoMin
            else:
                continue
        
        for genero in generos:
            duracao = 0
            for musica in self.musicas:
                if genero == musica.genero:
                    duracao += musica.duracaoMin
            
            print(f"{genero}: {duracao}")
        
metallica = Musica('One', 'Metallica', 6, 'Metal')
mastodon = Musica('Oblivion', 'Mastodon', 5, 'Metal')
korn = Musica('Falling Away from Me', 'Korn', 4, 'Nu Metal')
as_braba = Playlist('As Braba')

as_braba.adicionarMusica(metallica)
as_braba.adicionarMusica(mastodon)
as_braba.adicionarMusica(korn)

as_braba.listarMusicas()
as_braba.calculoTempo()
as_braba.tempoPorG()

as_braba.removerMusica(metallica)

as_braba.listarMusicas()
as_braba.calculoTempo()
as_braba.tempoPorG()