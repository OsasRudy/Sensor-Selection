class Divison:
    def divide_number(self, num1, num2):
         result = num1 / num2
         return result

class TestDivision:

    def test_if_number_is_divisible(self):
        # arrange
        num1 = 5
        num2 = -1
        # act
        result = Divison().divide_number(num1, num2)
        # assert
        assert result == -5

    def test_if_num2_is_bigger(self):
        # arrange
        num1 = 5
        num2 = 8
        # act
        result = Divison().divide_number(num1, num2)
        # assert
        assert result == 0.625

