import pytest
from app import Calculator as c

class TestCalc:
    def setup(self):
        self.calc = c

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 6) == 36

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 100, 10) == 10

    def test_subtraction_calculate_correcty(self):
        assert self.calc.subtraction(self, 100, 99) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 12, 10) == 22