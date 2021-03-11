"""
Unit testing the calculator app
"""

import basic_calculator


class TestBasicCalculator:

    def test_add(self):
        assert 5 == basic_calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == basic_calculator.subtract(5, 3)
