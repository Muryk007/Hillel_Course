import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from core.students import Students
from core.courses import Courses
from database import Session

def test_init_db_positive():
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/Hillel_Course_DB")
    engine = create_engine(db_url)

    try:
        connection = engine.connect()
        connection.close()
    except OperationalError:
        pytest.fail("Не вдалося підключитися до бази даних (перевір налаштування).")

def test_init_db_negative():
    bad_url = "postgresql://postgres:postgres@localhost:5432/Hillel_Course_DBB"
    engine = create_engine(bad_url)

    with pytest.raises(OperationalError):
        connection = engine.connect()
        connection.close()

@pytest.mark.parametrize(
    "student_name, student_age, course_id",
    [
        ('Joshua', 35, 1),
        ('Capone', 50, 2),
        ('Batman', 40, 3)
    ]
)
def test_add_student_positive(student_name, student_age, course_id):
    session = Session()

    existing = session.query(Students).filter_by(student_name=student_name, course_id=course_id).first()
    if existing:
        session.delete(existing)
        session.commit()

    student = Students(student_name=student_name, student_age=student_age, course_id=course_id)
    session.add(student)
    session.commit()
    session.refresh(student)

    found = session.query(Students).filter_by(student_name=student_name, course_id=course_id).first()
    assert found is not None
    assert found.student_age == student_age

    session.delete(found)
    session.commit()
    session.close()