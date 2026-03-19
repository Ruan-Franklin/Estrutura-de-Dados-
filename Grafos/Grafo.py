class Vertice:
    
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False 
        self.adjacentes = []
    
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
        
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)
class Aresta:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        

class Grafo:
  arad = Vertice('Arad')
  zerind = Vertice('Zerind')
  oradea = Vertice('Oradea')
  sibiu = Vertice('Sibiu')
  timisoara = Vertice('Timisoara')
  lugoj = Vertice('Lugoj')
  mehadia = Vertice('Mehadia')
  dobreta = Vertice('Dobreta')
  craiova = Vertice('Craiova')
  rimnicu = Vertice('Rimnicu')
  fagaras = Vertice('Fagaras')
  pitesti = Vertice('Pitesti')
  bucharest = Vertice('Bucharest')
  giurgiu = Vertice('Giurgiu')

  arad.adiciona_adjacente(Aresta(zerind, 75))
  arad.adiciona_adjacente(Aresta(sibiu, 140))
  arad.adiciona_adjacente(Aresta(timisoara, 118))

  zerind.adiciona_adjacente(Aresta(arad, 75))
  zerind.adiciona_adjacente(Aresta(oradea, 71))

  oradea.adiciona_adjacente(Aresta(zerind, 71))
  oradea.adiciona_adjacente(Aresta(sibiu, 151))

  sibiu.adiciona_adjacente(Aresta(oradea, 151))
  sibiu.adiciona_adjacente(Aresta(arad, 140))
  sibiu.adiciona_adjacente(Aresta(fagaras, 99))
  sibiu.adiciona_adjacente(Aresta(rimnicu, 80))

  timisoara.adiciona_adjacente(Aresta(arad, 118))
  timisoara.adiciona_adjacente(Aresta(lugoj, 111))

  lugoj.adiciona_adjacente(Aresta(timisoara, 111))
  lugoj.adiciona_adjacente(Aresta(mehadia, 70))

  mehadia.adiciona_adjacente(Aresta(lugoj, 70))
  mehadia.adiciona_adjacente(Aresta(dobreta, 75))

  dobreta.adiciona_adjacente(Aresta(mehadia, 75))
  dobreta.adiciona_adjacente(Aresta(craiova, 120))

  craiova.adiciona_adjacente(Aresta(dobreta, 120))
  craiova.adiciona_adjacente(Aresta(pitesti, 138))
  craiova.adiciona_adjacente(Aresta(rimnicu, 146))

  rimnicu.adiciona_adjacente(Aresta(craiova, 146))
  rimnicu.adiciona_adjacente(Aresta(sibiu, 80))
  rimnicu.adiciona_adjacente(Aresta(pitesti, 97))

  fagaras.adiciona_adjacente(Aresta(sibiu, 99))
  fagaras.adiciona_adjacente(Aresta(bucharest, 211))

  pitesti.adiciona_adjacente(Aresta(rimnicu, 97))
  pitesti.adiciona_adjacente(Aresta(craiova, 138))
  pitesti.adiciona_adjacente(Aresta(bucharest, 101))

  bucharest.adiciona_adjacente(Aresta(fagaras, 211))
  bucharest.adiciona_adjacente(Aresta(pitesti, 101))
  bucharest.adiciona_adjacente(Aresta(giurgiu, 90))