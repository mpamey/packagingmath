import mymath


class TestCalculator:

    def test_addition(self):
        assert 4 == mymath.add(2, 2)

    def test_subtraction(self):
        assert 2 == mymath.subtract(4, 2)

    def test_squareroot(self):
        assert 4 == mymath.squareroot(16)

    def test_division(self):
        assert 4 == mymath.division(8, 2)

    def test_multiplication(self):
        assert 4 == mymath.multiply(4, 1)
