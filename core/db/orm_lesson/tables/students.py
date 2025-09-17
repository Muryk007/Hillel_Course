from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db.orm_lesson.tables.base import Base
# Базовий клас для визначення моделей даних


# Визначення моделі даних (таблиці) за допомогою класу
class Students(Base):
    __tablename__ = 'students_orm'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String, nullable=False)
    student_age = Column(Integer)
    course_id = Column(Integer, ForeignKey("courses_orm.course_id"))

    # кожен студент належить одному курсу
    course = relationship("Courses", back_populates="students")
