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
    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
                
    
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
            
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)
            
    def excluir(self, no):
        if self._esta_vazia():
            return
        atual = self.raiz
        pai = self.raiz
        eh_esquerdo = True
        while atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                eh_esquerdo = True
                atual = atual.esquerdo
            else:
                eh_esquerdo = False
                atual = atual.direita
            if atual == None:
                return False
            
            if atual.esquerda == None and atual.direita == None: 
                if atual  == self.raiz:
                    self.raiz = None
                elif eh_esquerdo:
                    pai.esquerda = None
                else:
                    pai.direita = None
            
            elif atual.direita == None:
                if atual == self.raiz:
                    self.raiz = atual.esquerda
                elif eh_esquerdo:
                    pai.esquerda = atual.esquerda
                else:
                    pai.direita = atual.esquerda
            elif atual.esquerda == None:
                if atual == self.raiz:
                    self.raiz = atual.direita
                elif eh_esquerdo:
                    pai.esquerda = atual.direita
                else:
                    pai.direita = atual.direita
            else:
                sucessor = self.get_sucessor(atual)
                if atual == self.raiz:
                    self.raiz = sucessor
                elif eh_esquerdo:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
                sucessor.esquerda = atual.esquerda
            return True
                    
        def get_sucessor(self, no):
            pai_sucessor = no
            sucessor = no
            atual = no.direita
            while atual != None:
                pai_sucessor = sucessor
                sucessor = atual
                atual = atual.esquerda
            if sucessor != no.direita:
                pai_sucessor.esquerda = sucessor.direita
                sucessor.direita = no.direita
            return sucessor
        
                    
            
    

    def pos_ordem(self, no):
        self.pos_ordem(no.esquerda)
        self.pos_ordem(no.direita)
        print(no.valor)
            
    

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
arvore.excluir(14)

arvore.pesquisar(30).mostra_no()
