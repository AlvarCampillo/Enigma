import unittest
import Enigma

class ReflectorTest(unittest.TestCase):
    def test_reflejaOK(self):
        reflector = Enigma.Reflector()
        self.assertEqual(reflector.refleja("A"), "Z")

class RotorTest(unittest.TestCase):
    def test_construyeOK(self):
        rotor = Enigma.Rotor("ABCDEFG", "CFAGBDE")
        self.assertEqual(rotor.conexion, ["ABCDEFG", "CFAGBDE"])

    def test_codificaOK(self):
        rotor = Enigma.Rotor("ABCDEFG", "CFAGBDE")
        self.assertEqual(rotor.codifica(0), 2)
        self.assertEqual(rotor.decodifica(0), 2)
    
    def text_codificaOK_con_pos_ini(self):
        rotor = Enigma.Rotor("ABCDEFG", "CFAGBDE")
        rotor.pos_ini = "C"
        self.assertEqual(rotor.pos_ini, 2)
        self.assertEqual(rotor.codifica(0), 5)
        self.assertEqual(rotor.decodifica(0), 5)

if __name__ == "__main__":
    unittest.main()