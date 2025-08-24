# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = (360-self.angle_a*2)/2

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                print("side_a must be > 0. Value will set to 1")
                print("-"*20)
                value = 1
            super().__setattr__(key, value)

        elif key == "angle_a":
            if 0 < value < 180:
                super().__setattr__(key, value)
                super().__setattr__("angle_b", (360-value*2)/2)
            else:
                print("angle_a must be > 0 and < 180. Value will set to 179")
                print("-" * 20)
                value = 179
                super().__setattr__(key, value)
                super().__setattr__("angle_b", (360 - value * 2) / 2)
        else:
            super().__setattr__(key, value)

    def __eq__(self, other):
        if self.angle_a + self.angle_b == 180:
            pass
        else:
            print("Sum of angle_a and angle_b must be equal to 180")



rombus = Rhombus(0, 0)
print(rombus.side_a)
print(rombus.angle_a)
print(rombus.angle_b)
