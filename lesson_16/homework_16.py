# Завдання 1

# # Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
# а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника
# з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут
# team_size, який вказує на кількість розробників у команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
#
# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього
# декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по
# типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька
# різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.


class Employee:
    def __init__(self, name, salary, **kwargs)   :
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self,  department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name=name,
                         salary=salary,
                         department=department,
                         programming_language=programming_language)
        self.team_size = team_size

# lead = TeamLead("Oleh", 5000, "QA", "JS", 5)

# print(lead.name)
# print(lead.salary)
# print(lead.department)
# print(lead.programming_language)
# print(lead.team_size)