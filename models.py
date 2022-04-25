from database import Base, engine
from sqlalchemy import Column, Integer, Float, String, or_, update

class Student(Base):
    __tablename__ = 'Student'

    std_id = Column(String(50), primary_key=True)
    gov_id = Column(String(50))
    name = Column(String(50))
    surname = Column(String(50))
    major = Column(String(50))
    department = Column(String(50))

class Course(Base):
    __tablename__ = 'Course'

    course_id = Column(String(50), primary_key=True)
    name = Column(String(50))
    section = Column(Integer)
    credit = Column(Integer)
    str_time = Column(String(4))
    end_time = Column(String(4))

class Major(Base):
    __tablename__ = 'Major'

    major_id = Column(String(50), primary_key=True)
    name = Column(String(50))

class Department(Base):
    __tablename__ = 'Department'

    department_id = Column(String(50), primary_key=True)
    name = Column(String(50))

class Enroll(Base):
    __tablename__ = 'Enroll'

    enroll_id = Column(Integer, primary_key=True)
    std_id = Column(String(50))
    course_id = Column(String(50))
    section = Column(Integer)
    grade = Column(String(2))

Base.metadata.create_all(engine)