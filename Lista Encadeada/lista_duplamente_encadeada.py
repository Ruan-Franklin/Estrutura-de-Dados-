class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None 
        

class ListaDuplamenteEncadeada:
    def  __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
        
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.novo.anterior = self.ultimo
        self.ultimo = novo
        
    def mostrar_frente(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
            
    def mostrar_atras(self):
        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior
            
        