# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
print("-"*40, "Генератор № 1")

class ReturnPairNumbers_1():
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        for n in range(2, self.max_number + 1, 2):
            yield n

for number in ReturnPairNumbers_1(21):
    print(number)

# Генератори:
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
print("-"*40, "Генератор № 2")

class GenerateFibonacciSequence():
    def __init__(self, end_number):
        self.start_number = 1
        self.intermidiate_number = 0
        self.end_number = end_number

    def __iter__(self):
        while self.intermidiate_number <= self.end_number:
            yield self.intermidiate_number # віддаємо поточне число
            self.intermidiate_number, self.start_number = self.start_number, self.start_number + self.intermidiate_number # зсуваємо: тепер aintermidiate_number стає start_number, а start_number стає сумою start_та intermidiate_number

for number in GenerateFibonacciSequence(144):
    print(number)


# Ітератори
# Реалізуйте ітератор для зворотного виведення елементів списку.
print("-"*40, "Ітератор № 1")

class ReverseListIterator:
    def __init__(self):
        self.lst = input("Введи числа через пробіл: ")
        self.list_of_nums = [int(x) for x in self.lst.split()]
        self.index = len(self.list_of_nums) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.list_of_nums[self.index]
        self.index -= 1
        return value

my_nums = ReverseListIterator()

for num in my_nums:
    print(num)

# Ітератори:
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
print("-"*40, "Ітератор № 2")

class ReturnPairNumbers_2():
    def __init__(self, max_number):
        self.__current = 0
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        while self.__current < self.max_number:
            self.__current = self.__current + 1
            if self.__current % 2 == 0:
                return self.__current
        raise StopIteration

for number in ReturnPairNumbers_2(15):
    print(number)



# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
print("-"*40, "Декоратор № 1")
import logging

def log_decorator(fn):
    consoleHandler = logging.StreamHandler()

    logging.basicConfig(
        handlers=[consoleHandler],
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force = True
    )

    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        log_message = f"Аргумент 1: {args[0]}, Аргумент 2: {args[1]}, Результат: {result}"
        logger = logging.getLogger()
        logger.info(log_message)
        return result
    return wrapper


@log_decorator
def pythagorean_theorem(a, b):
    return pow(a, 2) + pow(b, 2)

pythagorean_theorem(2, 4)

# Декоратори:
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
print("-"*40, "Декоратор № 2")

def raise_exeptions(fn):
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args,**kwargs)
        except TypeError:
            print(f' "Не вдалось опрацювати один з аргументів. Аргумент 1: {args[0]} - {type(args[0])}. Аргумент 2: {args[1]} - {type(args[1])}"')
            return None
        return result
    return wrapper

@raise_exeptions
def pythagorean_theorem(a, b):
    return pow(a, 2) + pow(b, 2)

pythagorean_theorem(2, "4")