""" 
Enigma Code.

"""
import random

letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

class Rotor():

    def __init__(self, abecedario ="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.rotor = []
        otrasLetras = list(self.abecedario)
        for l in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)

        self.rotorC = self.rotor[:]

    
    def codifica(self, letra):
        pletra = self.abecedario.index(letra)
        return self.rotorC[pLetra][1]
        self.avanza()

        # Ver como cambiar el error para que salga bien, lo anterior devuelve -1    
        raise ValueError("{} no pertenece al abecedario".format(letra))

    def posicionInicial(self, letra):
        position = self.abecedario.index(letra)
        self.rotorC = self.rotor[position:] + self.rotor[:position]

    def avanza(self):
        self.rotorC = self.rotor[1:] + self.rotor[0]

Rotor()