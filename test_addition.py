import unittest

# Créez une fonction simple à tester.
def addition(a, b):
    return a + b


# TDD : Développement dirigé par les test (Test Driven Devloppement).
# Écrivez une méthode de test pour la fonction addition.

class TestAddition(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Définition du code de la méthode de test
    def test_addition(self):
        # Assertion pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(addition(2,3),5)
        self.assertEqual(addition(7,8),15)
        self.assertEqual(addition(9,3),12)
# Définition d'un objet de test
test_addition = unittest.TestLoader().loadTestsFromTestCase(TestAddition)    # Mettre comme argument le nom de la classe définit pour le test
# Exécution du test
unittest.TextTestRunner().run(test_addition)


