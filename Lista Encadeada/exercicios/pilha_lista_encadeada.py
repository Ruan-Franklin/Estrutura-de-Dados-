"""
Classe para criar uma pilha utilizando uma lista encadeada.
Deve-se usar lista encadeada simples
-A classe chamada PilhaListaEncadeada deve conter os seguintes métodos: empilhar, desempilhar, ver_topo, pilha_vazia
"""

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
class PilhaListaEncadeada:
    def __init__(self):
        self.topo = None
    
    
    def pilha_vazia(self):
        return self.topo == None
    
    def ver_topo(self):
        if self.pilha_vazia():
            return None
        return self.topo.valor
    
    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        
    def desempilhar(self):
        if self.pilha_vazia():
            return None
        valor_desempilhado = self.topo.valor
        self.topo = self.topo.proximo
        return valor_desempilhado
    
    def imprimir_pilha(self):
        if self.pilha_vazia():
            print("Pilha vazia")
            return
        no_atual = self.topo
        while no_atual is not None:
            print(no_atual.valor)
            no_atual = no_atual.proximo


pilha = PilhaListaEncadeada()
pilha.pilha_vazia()
pilha.empilhar(10)
pilha.empilhar(20)
pilha.imprimir_pilha()