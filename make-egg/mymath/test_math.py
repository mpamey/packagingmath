import mymath


class TestCalculator:

    def test_addition(self):
        assert 4 == mymath.add(2, 2)

    def test_subtraction(self):
        assert 2 == mymath.subtract(4, 2)
