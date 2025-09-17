import pytest
import logging
import logging.config

from sqlalchemy import create_engine
from core.db.orm_lesson.tables.students import Students
from sqlalchemy.exc import OperationalError

from lesson_22.homework_22 import Session

logging.basicConfig(
    filename='lesson_22/tests_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    force=True
)

def test_init_db_positive():
    PG_SQL = "postgresql://oleh.muratov@localhost:5432/Hillel_Course_DB"
    engine = create_engine(PG_SQL)
    try:
        connection = engine.connect()
        connection.close()
        logging.info("Тест: test_init_db_positive пройшов успішно. Зʼєднання з БД встановлено")
    except OperationalError:
        logging.error("Тест: test_init_db_positive провалився. Не вдалося підключитися до БД.")


def test_init_db_negative():
    PG_SQL = "postgresql://oleh.muratov@localhost:5432/Hillel_Course_DBB"
    engine = create_engine(PG_SQL)
    with pytest.raises(OperationalError):
        connection = engine.connect()
        connection.close()
        logging.info("Такої БД не існує")

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

    exists = session.query(Students).filter_by(student_name=student_name, course_id=course_id).first()

    if not exists:
        student = Students(student_name=student_name, student_age=student_age, course_id=course_id)
        session.add(student)
        session.commit()
        session.refresh(student)

    logging.info(f"Тест test_add_student_positive пройшов вдало")

    session.delete(student)
    session.commit()
    session.close()