def unique_1 (unique_chars):
    """
    Опрацьовуємо вхідну строку.
    Якщо унікальних символів більше 10, виводимо True.
    Якщо унікальних символів меньше 10, виводимо False.
    :param unique_chars:
    :return: True or False
    """
    if len(unique_chars) > 10:
        return True
    else:
        return False


def find_sum (massive):
    """
    Рахуємо суму чисел у кожному списку у масиві.
    Якщо список містить не тільки числа, то виводимо помилку.
    :param massive:
    :return: result or error
    """
    results = []
    for item in massive:
        try:
            numbers = [int(num.strip()) for num in item.split(",")]
            results.append(sum(numbers))
            # print(f'сума: {sum(numbers)}')
        except ValueError:
            raise ValueError(f' "Не вдалось опрацювати елементи: {item}"')
            # print(f' "Не вдалось опрацювати елементи: {item}"')
    return results

def verification_2 (sum_storages, first_second_storage, second_third_storage):
    """
    Треба вирахувати кількість товарів на кожному з трьох складів.
    Якщо відомо і можна ввести:
    1. кількість товарів на трьох складах
    2. кількість товарів на першому і другому складах
    3. кількість товарів на другому і третьому складах
    :return: повертаємо кількість товарів на кожному складі
    """
    try:
        sum_storages_2 = int(sum_storages)
    except ValueError:
        raise ValueError("Total quantity is not a number")

    try:
        first_second_storages_2 = int(first_second_storage)
    except ValueError:
        raise ValueError("Goods quantity in the first and second storages is not a number")

    try:
        second_third_storages_2 = int(second_third_storage)
    except ValueError:
        raise ValueError("Goods quantity in the second and third storages is not a number")

    first_storage_2 = sum_storages_2 - second_third_storages_2
    third_storage_2 = sum_storages_2 - first_second_storages_2
    second_storage_2 = sum_storages_2 - first_storage_2 - third_storage_2
    if first_storage_2 + second_storage_2 + third_storage_2 == sum_storages_2:
        return first_storage_2, second_storage_2, third_storage_2
    else:
        return False

def sum_duplicates(my_lst):
    """
    Рахуємо суму парних чисел
    :param my_lst:
    :return: сума
    """
    duplicates = []
    for item in my_lst:
            if item % 2 == 0:
                duplicates.append(item)
    return sum(duplicates)
