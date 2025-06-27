import unittest


def factorielle(n):
    """
    Calcule la factorielle d'un nombre entier positif n.

    Args:
    n (int): Nombre entier positif.

    Returns:
    int: Factorielle de n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("La factorielle n'est définie que pour les entiers positifs.")

    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


class TestFactorielle(unittest.TestCase):  # Héritage de la classe TestCase de unittest
    # Définition du code de la méthode de test
    def test_factorielle(self):
        # Assertions pour vérifier si le résultat est conforme à ce qui est attendu
        self.assertEqual(factorielle(0), 1)  # 0! = 1
        self.assertEqual(factorielle(1), 1)  # 1! = 1
        self.assertEqual(factorielle(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
        self.assertEqual(factorielle(3), 6)  # 3! = 3 * 2 * 1 = 6
        self.assertEqual(factorielle(7), 5040)  # 7! = 5040

    def test_factorielle_negative_ou_non_entier(self):
        # Test pour les entrées invalides (négatives ou non entières)
        with self.assertRaises(ValueError):
            factorielle(-1)
        with self.assertRaises(ValueError):
            factorielle(3.5)
        with self.assertRaises(ValueError):
            factorielle("abc")


# Définition d'un objet de test
test_factorielle = unittest.TestLoader().loadTestsFromTestCase(
    TestFactorielle)  # Mettre comme argument le nom de la classe définit pour le test
# Exécution du test
unittest.TextTestRunner().run(test_factorielle)