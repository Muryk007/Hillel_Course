import pytest

from homework_10 import unique_1
from homework_10 import find_sum
from homework_10 import verification_2
from homework_10 import sum_duplicates

class TestUniqueCharacters:
    def test_unigue_true(self):
        assert (unique_1("More than 10")) is True

    def test_unuque_false(self):
        assert (unique_1("< 10")) is False

class TestFindSum:
    def test_find_sum_true(self):
        massive = ["1,2,3", "5,6,7"]
        assert (find_sum(massive)) == [6, 18]

    def test_find_sum_false(self):
        massive = ["1, 2, 3", "4, 5, 6", "a7, b8, c9"]
        with pytest.raises(ValueError, match='Не вдалось опрацювати елементи: a7, b8, c9'):
            find_sum(massive)

@pytest.mark.dailyBuildsTests
class TestVerification:
    def test_verification_true(self):
        result = verification_2(375291, 250449, 222950)
        assert result == (152341, 98108, 124842)

    def test_verification_false_1(self):
        with pytest.raises(ValueError, match='Total quantity is not a number'):
            verification_2("sad132", 250449, 222950)

    def test_verification_false_2(self):
        with pytest.raises(ValueError, match='Goods quantity in the first and second storages is not a number'):
            verification_2(152341, "sds456", 222950)

    def test_verification_false_3(self):
        with pytest.raises(ValueError, match='Goods quantity in the second and third storages is not a number'):
            verification_2(152341, 250449, "22a2950")

@pytest.mark.skip(reason="duplicateTest")
class TestUniqueCharacters:
    def test_unigue_true(self):
        assert (unique_1("More than 10")) is True

@pytest.mark.customMark(reason="a new name")
class TestSumDuplicates:
    def test_sum_duplicates_true(self):
        result = sum_duplicates([2, 4, 6, 8, 10])
        assert result == 30

    def test_sum_duplicates_false(self):
        result = sum_duplicates([1, 3, 5, 7, 9])
        assert result == 0

# або з використанням декоратора parametrize
@pytest.mark.parametrize("input_list, expected", [
    ([2, 4, 6, 8, 10], 30),
    ([1, 3, 5, 7, 9], 0),
    ([0, 2, 5], 2)
])
def test_sum_duplicates(input_list, expected):
    assert sum_duplicates(input_list) == expected