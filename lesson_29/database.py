import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from core.base import Base
from core.students import Students
from core.courses import Courses

import logging.config
import pathlib

# Трішки змінив логер та підключення до БД
def init_log():
    log_path = pathlib.Path(__file__).parent / "logging.conf"
    if log_path.exists():
        logging.config.fileConfig(log_path)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.warning("logging.conf не знайдено — використовую базове логування.")


init_log()

def init_db():
    PG_SQL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/Hillel_Course_DB"
    )
    engine = create_engine(PG_SQL)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal


Session = init_db()

def default_values():
    session = Session()
    courses = ['Mathematics', 'Chemistry', 'Physics', 'ART', 'Philosophy']

    # Додаємо нові курси
    existing_courses = {c.course_name for c in session.query(Courses).all()}
    new_courses = [Courses(course_name=name) for name in courses if name not in existing_courses]
    session.add_all(new_courses)

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
    logging.info("Дефолтні дані ініціалізовано.")

def add_course(course_name: str):
    session = Session()
    exists = session.query(Courses).filter_by(course_name=course_name).first()
    if exists:
        logging.warning(f"Курс '{course_name}' вже існує.")
    else:
        session.add(Courses(course_name=course_name))
        session.commit()
        logging.info(f"Додано курс: {course_name}")
    session.close()

# INSERT - додаємо студента (сутність)
def add_student(name: str, age: int, course_id: int):
    session = Session()
    exists = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
    if exists:
        logging.warning(f"Студент '{name}' вже записаний на курс №{course_id}.")
    else:
        session.add(Students(student_name=name, student_age=age, course_id=course_id))
        session.commit()
        logging.info(f"Додано студента: {name}, курс: {course_id}")
    session.close()

# UPDATE - апдейтимо атрибути для однієї сутності з заданим імʼям
def upd_one_student_age(name: str, age: int, course_id: int):
    session = Session()
    student = session.query(Students).filter_by(student_name=name, course_id=course_id).first()
    if not student:
        logging.warning(f"Студента '{name}' (курс {course_id}) не знайдено.")
    else:
        student.student_age = age
        session.commit()
        logging.info(f"Оновлено вік студента {name} (курс {course_id}) → {age} років.")
    session.close()

# UPDATE - апдейтимо атрибути для усіх сутностей з заданим імʼям
def upd_all_student(name: str, age: int):
    session = Session()
    students = session.query(Students).filter_by(student_name=name).all()
    if not students:
        logging.warning(f"Студентів із іменем '{name}' не знайдено.")
    for student in students:
        student.student_age = age
    session.commit()
    session.close()
    logging.info(f"Усі '{name}' тепер мають {age} років.")

# JOIN - по course_id
def display_students_by_course(course_id: int):
    session = Session()
    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.course_id == course_id)
        .all()
    )
    for student, course in result:
        print(f"Студент: {student.student_name}, Вік: {student.student_age}, Курс: {course.course_name}")
    session.close()

# JOIN - за імʼям
def display_students_by_name(name: str):
    session = Session()
    result = (
        session.query(Students, Courses)
        .join(Courses, Students.course_id == Courses.course_id)
        .filter(Students.student_name == name)
        .all()
    )
    for student, course in result:
        print(f"Студент: {student.student_name}, Вік: {student.student_age}, Курс: {course.course_name}")
    session.close()

if __name__ == "__main__":
    default_values()
    add_course("Geometry")
    add_student("Oleh", 21, 3)
    upd_one_student_age("Oleh", 28, 3)
    upd_all_student("Oleh", 30)
    display_students_by_course(2)
    display_students_by_name("Oleh")