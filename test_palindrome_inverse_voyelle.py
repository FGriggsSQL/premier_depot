import unittest

# Définition de la formule de détermination d'un palindrome
def est_palindrome(chaine):
    # <(filter(str.isalnum, chaine))> : Ignore la casse et les espaces pour la vérification.
    # <"".join> et <.lower()> : retire les espaces et met la chaine en minuscules
    chaine_propre = "".join(filter(str.isalnum, chaine)).lower()

    # Vérifie si une chaîne de caractères est un palindrome.
    return chaine_propre == chaine_propre[::-1]

# Définition de la formule d'inversion d'une chaîne
def inverser_chaine(chaine):
    # Retourne l'inverse d'une chaîne de caractères.
    return chaine[::-1]

# Définition de la formule d'un compteur de voyelles
def compter_voyelles(chaine):
    # Compte le nombre de voyelles (a, e, i, o, u, y) dans une chaîne,
    # en ignorant la casse.

    voyelles = "aeiouy"
    compteur = 0
    for lettres in chaine:
        if lettres.lower() in voyelles:
            compteur += 1
    return compteur


class TestPalindromeInverseVoyelle(unittest.TestCase):

    # Définition du code de la méthode de test
    def test_est_palindrome(self):
        # Assertions pour vérifier si les résultats sont conformes à ce qui est attendu
        # Cas simples
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("ressasser"))
        self.assertTrue(est_palindrome("")) # Chaîne vide est un palindrome
        self.assertTrue(est_palindrome("a")) # Un seul caractère est un palindrome

        # Cas avec espaces et casse différente
        self.assertTrue(est_palindrome("Non"))
        self.assertTrue(est_palindrome("Racecar"))

        # Cas non-palindromes
        self.assertFalse(est_palindrome("bonjour"))
        self.assertFalse(est_palindrome("python"))
        self.assertFalse(est_palindrome("hello world"))

    # Définition du code de la méthode de test
    def test_inverser_chaine(self):
        # Assertions pour vérifier si les résultats sont conformes à ce qui est attendu
        self.assertEqual(inverser_chaine("bonjour"), "ruojnob")
        self.assertEqual(inverser_chaine("radar"), "radar")
        self.assertEqual(inverser_chaine("Python"), "nohtyP")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12345"), "54321")

    # Définition du code de la méthode de test
    def test_compter_voyelles(self):
        self.assertEqual(compter_voyelles("bonjour"), 3) # o, ou
        self.assertEqual(compter_voyelles("RADAR"), 2) # A, A
        self.assertEqual(compter_voyelles("Python"), 2) # o
        self.assertEqual(compter_voyelles("aeiouyAEIOUY"), 12) # Toutes les voyelles
        self.assertEqual(compter_voyelles("rhythm"), 1) # Pas de voyelle
        self.assertEqual(compter_voyelles(""), 0) # Chaîne vide
        self.assertEqual(compter_voyelles("bcdfghjklmnpqrstvwxz"), 0) # Que des consonnes

# Définition d'un objet de test
# Mettre comme argument le nom de la classe définit pour le test
test_suite_PalindromeInverseVoyelle = unittest.TestLoader().loadTestsFromTestCase(TestPalindromeInverseVoyelle)
# Exécution du test
unittest.TextTestRunner(verbosity=2).run(test_suite_PalindromeInverseVoyelle) # Exécute la suite de tests
