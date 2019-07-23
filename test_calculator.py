"""
Unit test for Calculator Library
"""
import calculator


class TestCalculator:
    def test_adding(self):
        assert 4 == calculator.add(1, 3)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)
