class No:
    def __init__(self, valor):
        self.proximo = None
        self.valor = valor

    def mostrar_no(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo

        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.__lista_vazia():
            print("Lista vazia")
            return
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo


lista = ListaEncadeadaExtremidadeDupla()

lista.insere_inicio((10))
lista.insere_inicio((20))
lista.mostrar()