import unittest

# Définition de la fonction pour calculer la puissance d'une variable.
def puissance(base, exposant):
    return base ** exposant

class TestPuissance(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Définition du code de la méthode de test
    def test_puissance(self):
        # Assertions pour vérifier si les résultats sont conformes à ce qui est attendu
        self.assertEqual(puissance(2, 3), 8)   # 2 élevé à la puissance 3 est 8
        self.assertEqual(puissance(7, 2), 49)  # 7 élevé à la puissance 2 est 49
        self.assertEqual(puissance(9, 0), 1)   # N'importe quel nombre élevé à la puissance 0 est 1
        self.assertEqual(puissance(5, 1), 5)   # N'importe quel nombre élevé à la puissance 1 est le nombre lui-même

# Définition d'un objet de test
test_puissance = unittest.TestLoader().loadTestsFromTestCase(TestPuissance)    # Mettre comme argument le nom de la classe définit pour le test
# Exécution du test
unittest.TextTestRunner().run(test_puissance)