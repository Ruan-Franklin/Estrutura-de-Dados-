class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostra_no(self):
        print(self.valor)

class ABP:
    def __init__(self):
        self.raiz = None
        
    def _esta_vazia(self):
        return self.raiz is None