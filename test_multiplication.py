import unittest

# Définition de la formule de multiplication de deux variables.
def multiplication(a, b):
    return a * b

class Testmultiplication(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Définition du code de la méthode de test
    def test_multiplication(self):
        # Assertion pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(multiplication(2,3),6)
        self.assertEqual(multiplication(7,8),56)
        self.assertEqual(multiplication(9,3),27)

# Définition d'un objet de test
test_multiplication = unittest.TestLoader().loadTestsFromTestCase(Testmultiplication)    # Mettre comme argument le nom de la classe définit pour le test
# Exécution du test
unittest.TextTestRunner().run(test_multiplication)

