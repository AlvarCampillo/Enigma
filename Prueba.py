
from Enigma import *

rotorP = [('A', 'C'), ('B', 'Y'), ('C', 'B'), ('D', 'A'), ('E', 'V'), ('F', 'U'), ('G', 'S'), ('H', 'X'), ('I', 'K'), ('J', 'R'), ('K', 'P'), ('L', 'G'), ('M', 'D'), ('N', 'N'), ('Ñ', 'L'), ('O', 'W'), ('P', 'M'), ('Q', 'Ñ'), ('R', 'I'), ('S', 'H'), ('T', 'Q'), ('U', 'Z'), ('V', 'F'), ('W', 'J'), ('X', 'E'), ('Y', 'O'), ('Z', 'T')]

r = Rotor()
r.rotor = rotorP

print(r.codifica("S"))

r.posicionInicial("S")
print(r.rotorC)
