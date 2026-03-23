import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__tamanho = 0
        self.__valores = np.empty(self.__capacidade, dtype=object)
        
    def vetor_cheio(self):
        return self.__tamanho == self.__capacidade
    
    def vetor_vazio(self):
        return self.__tamanho == 0
    
    def inserir(self, valor):
        if not self.vetor_cheio():
            i = self.__tamanho - 1
            while i >= 0 and self.__valores[i].distancia_objetivo > valor.distancia_objetivo:
                self.__valores[i + 1] = self.__valores[i]
                i -= 1
            self.__valores[i + 1] = valor
            self.__tamanho += 1
        else:
            print('Vetor cheio')
            
    def imprimer(self):
        for i in range(self.__tamanho):
            print(self.__valores[i].rotulo, self.__valores[i].distancia_objetivo) 
class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self .__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=object)
        
    def pilha_cheia(self):
        return self.__topo == self.__capacidade - 1
    
    def pilha_vazia(self):
        return self.__topo == -1
    
    def empilhar(self, valor):
        if not self.pilha_cheia():
            self.__topo += 1
            self.__valores[self.__topo] = valor
        else:
            print('Pilha cheia')
            
    def desempilhar(self):
        if self.pilha_vazia():
            print('Pilha vazia')
            return None
        else:
            temp = self.__valores[self.__topo]
            self.__topo -= 1
            return temp
    def ver_topo(self):
        if self.pilha_vazia():
            print('Pilha vazia')
            return None
        else:
            return self.__valores[self.__topo]
class Vertice:
    
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
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
  arad = Vertice('Arad', 366)
  zerind = Vertice('Zerind', 374)
  oradea = Vertice('Oradea', 380)
  sibiu = Vertice('Sibiu', 253)
  timisoara = Vertice('Timisoara', 329)
  lugoj = Vertice('Lugoj', 244)
  mehadia = Vertice('Mehadia', 241)
  dobreta = Vertice('Dobreta', 242)
  craiova = Vertice('Craiova', 160)
  rimnicu = Vertice('Rimnicu', 193)
  fagaras = Vertice('Fagaras', 178)
  pitesti = Vertice('Pitesti', 98)
  bucharest = Vertice('Bucharest', 0)
  giurgiu = Vertice('Giurgiu', 77)

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
  
  
class BuscaEmProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True 
        self.pilha = Pilha(20)
        self.pilha.empilhar(self.inicio)
        
    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'Topo: {topo.rotulo}')
        for aresta in topo.adjacentes:
            print(f"Topo é: {topo.rotulo}, aresta é: {aresta.vertice.rotulo}, já visitado? {aresta.vertice.visitado}")
            if aresta.vertice.visitado == False:
                aresta.vertice.visitado = True
                self.pilha.empilhar(aresta.vertice)
                print(f"Empilhando {aresta.vertice.rotulo}")
                self.buscar()
            print(f"Desempilhando {topo.rotulo}")
            print()
            

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
        
    def buscar(self, vertice):
        print("------------")
        print(f'Vertice atual: {vertice.rotulo}')
        vertice.visitado = True
        if vertice == self.objetivo:
            self.encontrado = True        
        else:
            vetor_ordenado = VetorOrdenado(len(vertice.adjacentes))
            for adjacente in vertice.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.inserir(adjacente.vertice)
                    
            if vetor_ordenado.__valores[0] is not None:
                self.buscar(vetor_ordenado.__valores[0])
                
                