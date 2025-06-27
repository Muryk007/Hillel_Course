alice_in_wonderland =(
    "Would you tell me, please, which way I ought to go from here?\n"
    "That depends a good deal on where you want to get to \u2014 said the Cat.\n"
    "I don't much care where \u2014 said Alice.\n"
    "Then it doesn't matter which way you go \u2014 said the Cat.\n"
    "So long as I get somewhere, Alice added as an explanation.\n"
    "Oh, you're sure to do that \u2014 said the Cat, \u2014 if you only walk long enough."
    )
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


for char in alice_in_wonderland:
    if char == "'":
        print(char)

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436402
azov_sea_square = 37800
black_and_azov_sea_square = azov_sea_square + black_sea_square

print(f"Площа Чорного та Азовськго морів дорівнює {black_and_azov_sea_square} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_storages = 375291
first_second_storages = 250449
second_third_storages = 222950
first_storage = sum_storages - second_third_storages
third_storage = sum_storages - first_second_storages
second_storage = sum_storages - first_storage - third_storage

def verification ():
    if first_storage + second_storage + third_storage == sum_storages:
        print(
            f"На першому складі {first_storage} товарів.\n"
            f"На другому складі {second_storage} товарів.\n"
            f"На третьому склады {third_storage} товарів."
        )
    else:
        print("Треба перерахувати")

verification()

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
payment_period = 18
pc_cost = monthly_payment * payment_period

print(f"Вартість компєютера складає {pc_cost} гривень.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(a, b, c, d, e, f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_cost = 4 * 274
middle_pizza_cost = 2 * 218
juice_cost = 4 * 35
cake_cost = 1 *350
water_cost = 3 * 21
total_cost = big_pizza_cost + middle_pizza_cost + juice_cost + cake_cost

print(f"Для замовлення буде потрібно {total_cost} гривень.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos_sum = 232
photos_on_one_page = 8
pages_amount = photos_sum / photos_on_one_page

print(f"Для розміщеня всіх фотографій, Ігорю знадобиться {int(pages_amount)} сторінок у фотоальбомі.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

Kharkiv_Budapest = 1600
tank_volume = 48
fuel_per_100 = 9
one_tank_distance = (tank_volume / fuel_per_100) * 100
print(f"Відстань, яку можна проїхати на одному баку палива дорівнює {round(one_tank_distance, 1)} км")

fuel_amount = Kharkiv_Budapest / 100 * fuel_per_100
print(f"Кількість палива на подорож дорівнює {round(fuel_amount, 1)} літра")

car_refueling = Kharkiv_Budapest / one_tank_distance
print(f"Кількість заправок буде {int(car_refueling)}")

