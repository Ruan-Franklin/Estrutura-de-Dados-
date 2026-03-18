class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostra_no(self):
        print("{", self.valor, "}", end="")

class ABP:
    def __init__(self):
        self.raiz = None
        
    def _esta_vazia(self):
        return self.raiz is None
    
    def inserir(self, valor):
        novo = No(valor)
        
        if self._esta_vazia():
            self.raiz = novo
            atual = self.raiz
            return
        else:
            atual = self.raiz
        while True:
            pai = atual
            if valor < atual.valor:
                atual = atual.esquerda
                if atual == None:
                    pai.esquerda = novo
                    return
            else:
                atual = atual.direita
                if atual == None:
                    pai.direita = novo
                    return
    

arvore = ABP()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print("Terminou?")