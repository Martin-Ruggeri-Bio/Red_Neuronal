import math
from re import A

class Neurona():
    def __init__(self):
        self.entrada_0 = 1
        self.entrada_1 = 0
        self.entrada_2 = 0
        self.peso_0 = 0.9
        self.peso_1 = 0.66
        self.peso_2 = -0.2
        self.salida_esperada = 1
        self.salida_real = 1
    
    def entrenamiento(self, grafo, cant):
        i = 0
        while i < cant:
            for lista in grafo:
                self.entrada_1 = lista[0]
                self.entrada_2 = lista[1]
                self.salida_esperada = lista[2]
                x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2)
                self.salida_real = 1/(1+math.exp(x*(-1)))
                variacion_abs = self.salida_esperada - self.salida_real
                variacion_rel = self.salida_real*(1-self.salida_real)*variacion_abs
                variacion_peso_0 = 0.1*self.entrada_0*variacion_rel
                self.peso_0 = self.peso_0 + variacion_peso_0
                variacion_peso_1 = 0.1*self.entrada_1*variacion_rel
                self.peso_1 = self.peso_1 + variacion_peso_1
                variacion_peso_2 = 0.1*self.entrada_2*variacion_rel
                self.peso_2 = self.peso_2 + variacion_peso_2
            i+=1
    
    def operar(self, a, b):
        self.entrada_1 = a
        self.entrada_2 = b
        x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2)
        return 1/(1+math.exp(x*(-1)))
