import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(capacidade, dtype=int)
        
    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)
    
    def __deque_vazio(self):
        return self.numero_elementos == 0
    
    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print("Deque cheio!")
            return
        
        if self.__deque_vazio():
            self.inicio = 0
            self.final = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1
        self.valores[self.inicio] = valor
        self.numero_elementos += 1
        
    def insere_final(self, valor):
        if self.__deque_cheio():
            print("Deque cheio!")
            return
        
        if self.__deque_vazio():
            self.inicio = 0
            self.final = 0
        #Se o final estiver na última posição, remaneja os indices
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1
        self.numero_elementos += 1
        self.valores[self.final] = valor
        
        def excluir_inicio(self):
            if self.__deque_vazio():
                print("Deque vazio!")
                return
            
            if self.inicio == self.final:
                self.inicio = -1
                self.final = -1
            else:
                #VOlta para a posição inicial
                if self.inicio == self.capacidade -1:
                    self.inicio = 0
                else:
                    #Incrementar início para remover o início atual
                    self.inicio += 1
            self.numero_elementos -= 1
            
        def excluir_final(self):
            if self.__deque_vazio():
                print("Deque vazio!")
                return
            
            if self.inicio == self.final:
                self.inicio = -1
                self.final = -1
            elif self.inicio == 0:
                self.final = self.capacidade -1
            else:
                self.final -= 1
            self.numero_elementos -= 1
            
        
        def get_inicio(self):
            if self.__deque_vazio():
                print("Deque vazio!")
                return None
            return self.valores[self.inicio]
        
        def get_final(self):
            if self.__deque_vazio():
                print("Deque vazio!")
                return None
            return self.valores[self.final]
                 

            
                
            
            

        
        
        