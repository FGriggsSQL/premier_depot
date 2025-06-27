import unittest

# Définition de la fonction pour calculer la somme des entiers inférieurs à n.
def somme_entiers_inferieurs(n):
    if n <= 1:
        return 0  # La somme des entiers inférieurs à 1 ou 0 est 0
    else:
        # Utilisation de la formule de la somme des n-1 premiers entiers: (n-1) * n / 2
        # Version boucle for
        somme = 0
        for i in range(n): # Range va de 0 à n-1, ce qui inclut tous les entiers inférieurs à n
            somme += i
        return somme

class TestSommeEntiersInferieurs(unittest.TestCase):    # Héritage de la classe TestCase de unittest
    # Définition du code de la méthode de test
    def test_somme_entiers_inferieurs(self):
        # Assertions pour vérifier si les résultats sont conformes à ce qui est attendu
        self.assertEqual(somme_entiers_inferieurs(5), 10)  # Somme de 0+1+2+3+4 = 10
        self.assertEqual(somme_entiers_inferieurs(1), 0)   # Aucun entier inférieur à 1 (positif)
        self.assertEqual(somme_entiers_inferieurs(0), 0)   # Aucun entier inférieur à 0 (positif)
        self.assertEqual(somme_entiers_inferieurs(10), 45) # Somme de 0 à 9 = 45
        self.assertEqual(somme_entiers_inferieurs(2), 1)   # Somme de 0+1 = 1

# Définition d'un objet de test
test_somme_entiers_inferieurs = unittest.TestLoader().loadTestsFromTestCase(TestSommeEntiersInferieurs)    # Mettre comme argument le nom de la classe définit pour le test
# Exécution du test
unittest.TextTestRunner().run(test_somme_entiers_inferieurs)