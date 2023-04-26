"""Test file for testing the main.py file"""

import unittest
from unittest.mock import patch
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", side_effect=["1", "1", "1"])
    def test_1_1_1(self, _mock_input):
        """Testa se o programa responde "Equilátero" quando o usuário digita 1, 1, 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["5", "5", "5"])
    def test_5_5_5(self, _mock_input):
        """Testa se o programa responde "Equilátero" quando o usuário digita 5, 5, 5"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "2", "3"])
    def test_1_2_3(self, _mock_input):
        """Testa se o programa responde "Não é um triângulo" quando o usuário digita 1, 2, 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["3", "2", "1"])
    def test_3_2_1(self, _mock_input):
        """Testa se o programa responde "Não é um triângulo" quando o usuário digita 3, 2, 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "2", "4"])
    def test_1_2_4(self, _mock_input):
        """Testa se o programa responde "Escaleno" quando o usuário digita 1, 2, 4"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Escaleno", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["4", "2", "1"])
    def test_4_2_1(self, _mock_input):
        """Testa se o programa responde "Escaleno" quando o usuário digita 4, 2, 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Escaleno", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "1", "4"])
    def test_1_1_4(self, _mock_input):
        """Testa se o programa responde "Isósceles" quando o usuário digita 1, 1, 4"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "4", "1"])
    def test_1_4_1(self, _mock_input):
        """Testa se o programa responde "Isósceles" quando o usuário digita 1, 4, 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["4", "1", "1"])
    def test_4_1_1(self, _mock_input):
        """Testa se o programa responde "Isósceles" quando o usuário digita 4, 1, 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
