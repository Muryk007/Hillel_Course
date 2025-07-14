from statistics import median
import re

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    # while multiplier <= number: # табличку для чисел 1, 2, 3 та 4, при такій умові, надрукує лише до 1, 4, 9 та 16.
    while multiplier <= number or multiplier >= number: # при такій, до максимального значення добутку 25 для всіх чисел
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

    #     # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

def sum_numbers(num_1, num_2):
    print(str(num_1) + "+" + str(num_2) + "=" + str(num_1 + num_2))

sum_numbers(num_1, num_2)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def arithmetic_average(lst_1):
    print(median(lst_1))

    # or
    sum_1 = 0
    for num in lst_1:
        sum_1 = sum_1 + num
    print(sum_1 / len(lst_1))

arithmetic_average(lst_1)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
my_str_1 = input("Enter your text: ")

def reverse_text(my_str_1):
    my_str_1 = my_str_1[::-1]
    print(my_str_1)

reverse_text(my_str_1)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

text_input = input("Enter your text: ")
new_text = re.sub(r'[^\w\s]', '', text_input) # re.sub видаляє усі символи, окрім букв та цифр
lst_2 = new_text.split()

def longest_word(lst_2):
    max_len = 0
    longest = ""
    for word in lst_2:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    return longest
print(longest_word(lst_2))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# option 1
def verification (sum_storages, first_second_storages, second_third_storages):
    """
    Треба вирахувати кількість товарів на кожному з трьох складів.
    Якщо відомо:
    :param sum_storages: сума товарів на трьох складах
    :param first_second_storages: сума товарів на першому і другому складах
    :param second_third_storages: сума товарів на другому і третьому складах
    :return: повертаємо кількість товарів на кожному складі
    """
    first_storage = sum_storages - second_third_storages
    third_storage = sum_storages - first_second_storages
    second_storage = sum_storages - first_storage - third_storage
    if first_storage + second_storage + third_storage == sum_storages:
        print(
            f"На першому складі {first_storage} товарів.\n"
            f"На другому складі {second_storage} товарів.\n"
            f"На третьому складі {third_storage} товарів."
        )
    else:
        print("Треба перерахувати")
verification(375291, 250449, 222950)

# option 2
def verification_2 ():
    """
    Треба вирахувати кількість товарів на кожному з трьох складів.
    Якщо відомо і можна ввести:
    1. кількість товарів на трьох складах
    2. кількість товарів на першому і другому складах
    3. кількість товарів на другому і третьому складах
    :return: повертаємо кількість товарів на кожному складі
    """
    input_sum = input("Enter total quantity of goods: ")
    input_first_second = input("Enter goods quantity in the first and second storages: ")
    input_second_third = input("Enter goods quantity in the second and third storages: ")
    try:
        sum_storages_2 = int(input_sum)
    except ValueError:
        print("Total quantity is not a number")
    try:
        first_second_storages_2 = int(input_first_second)
    except ValueError:
        print("Goods quantity in the first and second storages is not a number")
    try:
        second_third_storages_2 = int(input_second_third)
    except ValueError:
        print("Goods quantity in the second and third storages is not a number")

    first_storage_2 = sum_storages_2 - second_third_storages_2
    third_storage_2 = sum_storages_2 - first_second_storages_2
    second_storage_2 = sum_storages_2 - first_storage_2 - third_storage_2
    if first_storage_2 + second_storage_2 + third_storage_2 == sum_storages_2:
        print(
            f"На першому складі {first_storage_2} товарів.\n"
            f"На другому складі {second_storage_2} товарів.\n"
            f"На третьому складі {third_storage_2} товарів."
        )
    else:
        print("Треба перерахувати")

verification_2()

# task 8
def upper_letter_count():
    """
    Функція рахує кількість слів, котрі починаються з великої літери та повертає їх кількість.
    :return: кількість слів, котрі починаються з великої літери
    """

    user_input = input("Enter your text: ")
    words = user_input.split()
    count = 0
    for word in words:
        if word[0].isupper():
            count += 1
    if count == 0 or count > 4:
        print(f'У тексті {count} слів, котрі починаються з великої літери')
    elif count == 1:
        print(f'У тексті {count} слово, котре починається з великої літери')
    else:
        print(f'У тексті {count} слова, котрі починаються з великої літери')

upper_letter_count()

task 9
car_data = {
'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria = (2017, 1.6, 36000)

def new_car_data(search_criteria: tuple):
    """
    Функція сортує авто з вже наявного кортежу за зростанням ціни та критеріями пошуку (рік ≥, об'єм двигуна ≥, ціна ≤)
    :param search_criteria: (рік, об'єм двигуна, ціна)
    :return: новий кортеж списків відсортованих авто
    """
    year_min, engine_min, price_max = search_criteria
    new_dict_cars = {}

    for i, (color, year, engine, body, price) in car_data.items():
        if year >= year_min and engine >= engine_min and price <= price_max:
            new_dict_cars[i] = (color, year, engine, body, price)

    new_list_cars = list(sorted(new_dict_cars.items(), key=lambda item: item[0][-1]))
    return new_list_cars[0:5]

print(new_car_data(search_criteria))

# task 10
chars = input("Enter the text and I'll count the unique characters in it: ")
unique_chars = set(chars)

def unique (unique_chars):
    """
    Функцыя рахуэ кількість унікальних символів в строці.
    Якщо їх більше 10 - виводить в консоль True, інакше - False.
    Строку отримуємо за допомогою функції input()
    :param unique_chars: приймає input та обробляється методом set
    :return: True або False
    """
    if len(unique_chars) > 10:
        return True
    else:
        return False
print(unique(unique_chars))