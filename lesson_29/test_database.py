import os
import pytest
import allure
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from core.students import Students
from core.courses import Courses
from database import Session

@allure.feature("Позитивний запуск БД")
def test_init_db():
    #def test_init_db_positive():
    with allure.step("Отримуємо URL бази даних з оточення"):
        db_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/Hillel_Course_DB")

    with allure.step("Створюємо engine SQLAlchemy"):
        engine = create_engine(db_url)

    with allure.step("Підключаємося до бази"):
        try:
            connection = engine.connect()
            connection.close()
        except OperationalError:
            pytest.fail("Не вдалося підключитися до бази даних (перевір налаштування).")

@allure.feature("Негативний запуск БД")
def test_init_db_negative():
    with allure.step("Формуємо неправильний URL для БД"):
        bad_url = "postgresql://postgres:postgres@localhost:5432/Hillel_Course_DBB"

    with allure.step("Створюємо engine SQLAlchemy"):
        engine = create_engine(bad_url)

    with allure.step("Очікуємо помилку при підключенні"):
        with pytest.raises(OperationalError):
            connection = engine.connect()
            connection.close()

@allure.feature("Робота зі студентами")
@pytest.mark.parametrize(
    "student_name, student_age, course_id",
    [
        ('Joshua', 35, 1),
        ('Capone', 50, 2),
        ('Batman', 40, 3)
    ]
)
def test_add_student_positive(student_name, student_age, course_id):
    with allure.step("Ініціалізуємо сесію БД"):
        session = Session()

    with allure.step(f"Перевіряємо, чи існує студент '{student_name}'"):
        existing = session.query(Students).filter_by(student_name=student_name, course_id=course_id).first()
        if existing:
            session.delete(existing)
            session.commit()

    with allure.step(f"Додаємо нового студента '{student_name}'"):
        student = Students(student_name=student_name, student_age=student_age, course_id=course_id)
        session.add(student)
        session.commit()
        session.refresh(student)
    with allure.step("Перевіряємо, що студент збережений у базі"):
        found = session.query(Students).filter_by(student_name=student_name, course_id=course_id).first()
        assert found is not None
        assert found.student_age == student_age

    with allure.step("Видаляємо тестового студента після перевірки"):
        session.delete(found)
        session.commit()
        session.close()