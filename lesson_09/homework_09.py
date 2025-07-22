def unique (unique_chars):
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

def new_car_data(search_criteria: tuple):
    """
    робимо вибірку автомобілей зі списку по search_criteria
    :param search_criteria:
    :return: новий список атомобілей
    """
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
    year_min, engine_min, price_max = search_criteria
    new_dict_cars = {}

    for i, (color, year, engine, body, price) in car_data.items():
        if year >= year_min and engine >= engine_min and price <= price_max:
            new_dict_cars[i] = (color, year, engine, body, price)

    new_list_cars = list(sorted(new_dict_cars.items(), key=lambda item: item[0][-1]))
    return new_list_cars[0:5]

def specific_persons(people_records):
    """
    Перевіряємо що у новий список додаються люди
    котрим більше або є 30 років і котрі йдуть під
    номерами 5, 9 та 12
    :return: новий список
    """
    persons = people_records[6], people_records[10], people_records[13]
    new_list = []
    for person_age in persons:
        age = person_age[2]
        if age >= 30:
            new_list.append(person_age)
    return new_list

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
        # print(
        #     f"На першому складі {first_storage_2} товарів.\n"
        #     f"На другому складі {second_storage_2} товарів.\n"
        #     f"На третьому складі {third_storage_2} товарів."
        # )
    else:
        return False
        # print("Треба перерахувати")