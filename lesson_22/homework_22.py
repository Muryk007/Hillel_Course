from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from core.db.orm_lesson.tables.base import Base
from core.db.orm_lesson.tables.courses import Courses
from core.db.orm_lesson.tables.students import Students

import logging.config
import pathlib

def init_log():
    log_path = pathlib.Path(__file__).parent / "logging.conf"
    logging.config.fileConfig(log_path, disable_existing_loggers=False)
    logging.config.fileConfig(log_path)

init_log()

# ТЗ:
# Створення моделі даних: Створіть просту модель даних для системи управління студентами. Модель може містити таблиці
# для студентів, курсів та їх відношень. Кожен студент може бути зареєстрований на декілька курсів.
# Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.

# Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
# Переконайтеся, що ці зміни коректно відображаються у базі даних.

# Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний
# курс, або курси, на які зареєстрований певний студент.

# Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення
# студентів з бази даних.

# Можна використовувати будь яку ORM на Ваш вібир

# Ініціалізація бази даних
def init_db():

    PG_SQL = "postgresql://oleh.muratov@localhost:5432/Hillel_Course_DB"
    engine = create_engine(PG_SQL)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session

Session = init_db()

def default_values():
    session = Session()

    # додаємо дефолтні курси
    courses = [
        'Mathematics',
        'Chemistry',
        'Physics',
        'ART',
        'Philosophy',
    ]

    # робимо перевірку, що однакових курсів не має
    existing_courses = {c.course_name for c in session.query(Courses).all()}
    add_courses = [Courses(course_name=name) for name in courses if name not in existing_courses]

    session.add_all(add_courses)

    # додаємо дефолтних студентів
    students = [
        ('John', 21, 1),
        ('Oleh', 22, 2),
        ('Ivan', 23, 3),
        ('Julian', 24, 4),
        ('Julia', 25, 5),
        ('Vladimir', 18, 2),
        ('Jacob', 19, 4),
        ('Ihor', 20, 4),
        ('Petr', 21, 5),
        ('Vadim', 22, 1),
        ('Den', 23, 2),
        ('Irina', 24, 3),
        ('Juliana', 25, 5),
        ('Vasyl', 18, 1),
        ('Andrii', 19, 1),
        ('Ekaterina', 20, 2),
        ('Kate', 21, 5),
        ('Serhii', 22, 4),
        ('Anastasia', 23, 3),
        ('Karlo', 24, 1),
        ('Sirena', 25, 4)
    ]

    # робимо перевірку, що один студент не може мати курси з однаковим id
    for name, age, course_id in students:
        exists = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
        if not exists:
            session.add(Students(student_name=name, student_age=age, course_id=course_id))

    session.commit()
    session.close()

default_values()

def add_course(course_name):
    session = Session()
    #course = [(course_name)]

    # робимо перевірку, що однакових курсів не має
    existing_courses = session.query(Courses).filter_by(course_name=course_name).first()
    if existing_courses:
        logging.error(f"Курс {course_name} вже існує")
    else:
        course = Courses(course_name=course_name)
        session.add(course)
        session.commit()
        logging.info(f"До бази даних Courses_orm був доданий курс: {course_name}")

    session.close()

add_course('Geometry')

# INSERT - додаємо студента (сутність)
def add_student(name, age, course_id):
    session = Session()
    student = [(name, age, course_id)]

    # робимо перевірку, що один студент не може мати курси з однаковим id
    for name, age, course_id in student:
        exists = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
        logging.error(f"Не вдалось додати студента {name}. На курсі №{course_id} вже є такий студент.")
        if not exists:
            session.add(Students(student_name=name, student_age=age, course_id=course_id))
            logging.info(f"До бази даних Students_orm був доданий студент: {name}, вік: {age}, курс: {course_id}")

    session.commit()
    session.close()

add_student('Oleh', 21, 3)

# UPDATE - апдейтимо атрибути для однієї сутності з заданим імʼям
def upd_one_student_age(name, age, course_id):
    session = Session()
    # фільтруємо по name та course_id
    # фільтрацію можна змінити за бажанням
    student = session.query(Students).filter_by(student_name=name, course_id=course_id).first()

    # атрибут який будемо апдейтити
    student.student_age = age
    logging.info(f"Студенту {name} з курсу №{course_id} було змінено вік на {age}")

    session.commit()
    session.close()

upd_one_student_age("Oleh", 28, 3)

# UPDATE - апдейтимо атрибути для усіх сутностей з заданим імʼям
def upd_all_student(name,age):
    session = Session()
    students = session.query(Students).filter_by(student_name=name).all()

    # цикл котрий перебирає усіх студентів по заданому імені та робить апдейт
    for student in students:
        student.student_age = age
    logging.info(f"Усім студентам з імʼям: {name} було змінено вік на: {age}")

    session.commit()
    session.close()

upd_all_student("Oleh",30)

# JOIN - по course_id
def display_students(course_id):
    session = Session()

    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.course_id == course_id) .all()
    )

    for student, course in result:
        print(f"Студент: {student.student_name}, Вік: {student.student_age}, Курс: {course.course_name}")

    print("-" * 20)
    session.close()

display_students(2)

# JOIN - за імʼям
def display_students(name):
    session = Session()

    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.student_name == name) .all()
    )

    for student, course in result:
        print(f"Студент: {student.student_name}, Вік: {student.student_age}, Курс: {course.course_name}")

    session.close()

display_students("Oleh")