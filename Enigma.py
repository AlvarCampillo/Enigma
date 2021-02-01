            #-----------------#
            #    ENIGMA I     #
            #-----------------#
            #    by Álvar     #
            #-----------------#
            #     ʕ•ᴥ•ʔ       #
            #-----------------#

# Importación de librerias necesarias
import random

letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Definimos el reflector
class Reflector():
    def __init__(self, conf = ["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", "ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"]):
        """
            si conf viene vacio, crear 1 (necesitamos un abecedario)
            si conf viene lleno, comprobar que cumple las especificaciones
        """
        self.configuracion = conf 

    def refleja(self, letra_entrada):
        posE = self.configuracion[0].index[letra_entrada]
        return self.configuracion[1][posE]

    """
    TODO:
        Configuración: - Lista de pares del abecedario.
        - Solo se repite 1 si la longitud es impar.
        - Es biunivoca
        - Métodos: refleja(letra_entrada) -> letra

    """
# Definimos el rotor
class Rotor():
    def __init__(self, abecedario, cortocircuito = None):
        self.conexion = [abecedario, cortocircuito]
        self.pos_ini = None

    def codifica(self, indice):
        letra = self.conexion[0][indice]
        indice_izda = self.conexion[1].index(letra)
        return indice_izda

    def decodifica(seld, indice):
        letra = self.conexion[1][indice]
        indice_dcha = self.conexion[0].index(letra)
        return indice_dcha
    
    @property
    def pos_ini(self):
        return self._pos_ini
    
    @pos_ini.setter
    def pos_ini(self, value):
        self._pos_ini = self.conexion[0].index(value)
        # transformar codifica y decodifica para jugar con estas cosas de property y setter

    """
    TODO:
        -Conexión: Lista de cadenas (abecedario cortocircuito) 
            que determina la salida según el caracter de salida o entrada
        - Posición: Índice/caracter en posición cero la conexión
        - Pasos ¿?: Número de pasos girados desde que se empieza a codificar
        - Salto: Índice, caracter de abecedario en que se obliga al salto del 
            siguiente rotor si lo hubiera.
        - swSalto: True o False.
        - codifica(Pin de entrada) -> Número de salida
        - decodifica(Pin de salida) -> Número de entrada a las bombillas
        - avanza(): Rota una posición la conexión y comprueba si debe activar swSalto
    """

# Definimos Enigma
class Enigma():
    pass
    """
    TODO:
        - reflector: su configuración prefijada en principio
        - rotor: su conexión prefijada en principio
        - posi_inicial: Letra del rotor (indice?)
        - codifica(mensaje): transforma el mensaje en uno nuevo, solo hay
            una dirección. Si se pasa la salida de codifica como entrada volviendo la posi_inicial
            se obtiene la otra entrada.
    """