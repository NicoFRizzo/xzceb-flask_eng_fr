import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_one_e2f(self):
        respopnse = translator.english_to_french('IBM Translator')
        self.assertEqual(respopnse, 'Traducteur IBM')
    
    def test_un_f2e(self):
        respopnse = translator.french_to_english('Traducteur IBM')
        self.assertEqual(respopnse, 'IBM Translator')
    
    def test_hello_2f(self):
        respopnse = translator.english_to_french('Hello')
        self.assertEqual(respopnse, 'Bonjour')

    def test_bonjour_2e(self):
        respopnse = translator.french_to_english('Bonjour')
        self.assertEqual(respopnse, 'Hello')
    
if __name__ == "__main__":
    unittest.main()