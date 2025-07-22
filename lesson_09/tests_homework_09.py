import unittest

from homework_09 import unique
from homework_09 import find_sum
from homework_09 import new_car_data
from homework_09 import specific_persons
from homework_09 import sum_duplicates
from homework_09 import verification_2

# unique
class TestUniquePositive(unittest.TestCase):
    def test_unique_more(self):
        self.assertTrue(unique("More that 10"))

class TestUniqueNegative(unittest.TestCase):
    def test_unique_less(self):
        self.assertFalse(unique("< 10"))

# find_sum
class TestFindSumFromMassivePositive(unittest.TestCase):
    def test_find_sum(self):
        massive = ["1,2,3", "5,6,7"]
        self.assertEqual(find_sum(massive), [6, 18])

class TestFindSumFromMassiveNegative(unittest.TestCase):
    def test_find_sum(self):
        massive = ["1,2,3", "5,6,7", "asd,3,2"]
        with self.assertRaises(ValueError):
            find_sum(massive)

# new_car_data
class TestNewCarData(unittest.TestCase):
    def test_new_car_data_positive(self):
        search_criteria = (2017, 1.6, 36000)
        result = new_car_data(search_criteria)
        self.assertTrue(all(car[1][1] >= 2017 and car[1][2] >= 1.6 and car[1][4] <= 36000 for car in result))

    def test_new_car_data_negative(self):
        search_criteria = (2030, 1.6, 36000)
        result = new_car_data(search_criteria)
        self.assertEqual(result, [])

# specific_persons
class TestSpecificPersons(unittest.TestCase):
    def test_specific_persons_positive(self):
        people_records = [
            ('John', 'Doe', 28, 'Engineer', 'New York'),
            ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
            ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
            ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
            ('Michael', 'Brown', 22, 'Student', 'Seattle'),
            ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
            ('David', 'Miller', 33, 'Software Developer', 'Austin'),
            ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
            ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
            ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
            ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
            ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
            ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
            ('Ava', 'White', 42, 'Journalist', 'San Diego'),
            ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
        ]
        self.assertTrue(specific_persons(people_records))

    def test_specific_persons_negative(self):
        people_records = [
            ('John', 'Doe', 28, 'Engineer', 'New York'),
            ('Alice', 'Smith', 5, 'Teacher', 'Los Angeles'),
            ('Bob', 'Johnson', 5, 'Doctor', 'Chicago'),
            ('Emily', 'Williams', 3, 'Artist', 'San Francisco'),
            ('Michael', 'Brown', 29, 'Student', 'Seattle'),
            ('Sophia', 'Davis', 4, 'Lawyer', 'Boston'),
            ('David', 'Miller', 3, 'Software Developer', 'Austin'),
            ('Olivia', 'Wilson', 7, 'Marketing Specialist', 'Denver'),
            ('Daniel', 'Taylor', 8, 'Architect', 'Portland'),
            ('Grace', 'Moore', 2, 'Graphic Designer', 'Miami'),
            ('Samuel', 'Jones', 5, 'Business Consultant', 'Atlanta'),
            ('Emma', 'Hall', 3, 'Chef', 'Dallas'),
            ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
            ('Ava', 'White', 4, 'Journalist', 'San Diego'),
            ('Ethan', 'Anderson', 3, 'Product Manager', 'Phoenix')
        ]
        self.assertFalse(specific_persons(people_records))

# sum_duplicates
class TestSumDuplicates(unittest.TestCase):
    def test_sum_duplicates_positive(self):
        my_lst = [2, 4, 6, 8, 10, 12, 14, 10, 12, 14]
        self.assertEqual(sum_duplicates(my_lst), 92)

    def test_sum_duplicates_negative(self):
        my_lst = [1, 3, 5, 7, 9, 11, 13, 15]
        self.assertFalse(sum_duplicates(my_lst))

class TestVerification(unittest.TestCase):
    def test_verification_positive(self):
        result = verification_2(375291, 250449, 222950)
        self.assertTrue(result)

    def test_verification_negative(self):
        with self.assertRaises(ValueError):
            verification_2('adb', 250449, 222950)

if __name__ == '__main__':
    unittest.main()

