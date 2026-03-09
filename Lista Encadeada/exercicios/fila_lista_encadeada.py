"""
Use uma lista encadeada com extremidades duplas para controlar o inicio e o final da fila
Crie uma nova classe chamada FilaEncadeada com os seguintes métodos:
 - enfileirar
 - desenfileirar
 - fila_vazia
 - ver_inicio
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
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
        novo.anterior = self.ultimo
        self.ultimo = novo
        
    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                print("Valor não encontrado")
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
            
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual
    

class FilaEncadeada:
    def __init__(self):
        self.lista = ListaDuplamenteEncadeada()
    
    def enfileirar(self, valor):
        self.lista.insere_final(valor)
        
    
    def imprimir(self):
        atual = self.lista.primeiro
        while atual != None:
            print(atual.valor)
            atual = atual.proximo
    
    def desenfileirar(self):
        return self.lista.excluir_inicio()
    
    def fila_vazia(self):
        return self.lista._ListaDuplamenteEncadeada__lista_vazia()
    
    def ver_inicio(self):
        if self.fila_vazia():
            print("Fila vazia")
            return None
        return self.lista.primeiro.valor    


fila = FilaEncadeada()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.imprimir()