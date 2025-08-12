class Student:
    def __init__(self, first_name, second_name, age):
        self.name = first_name
        self.second_name = second_name
        self.age = age
        self.average_score = 0

    def av_score(self, score, lessons):
        self.average_score = score/lessons
        return self.average_score


first_year_student = Student(first_name = "Ivan", second_name = "Ivanov", age = 18)
second_year_student = Student(first_name = "Oleksandr", second_name = "Oleksandrov", age = 20)

print(first_year_student.av_score(80, 10))
print(second_year_student.av_score(180, 15))