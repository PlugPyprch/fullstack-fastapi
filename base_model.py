from pydantic import BaseModel

class Base_Student(BaseModel):
    student_id: str
    gov_id: str
    name: str
    surname: str
    major: str
    department: str

class Base_Course(BaseModel):
    course_id: str
    name : str
    section : int
    credit : int
    str_time : str
    end_time : str

class Base_Major(BaseModel):
    major_id : str
    name : str

class Base_Department(BaseModel):
    department_id : str
    name : str

class Base_Enroll(BaseModel):
    enroll_id : int
    std_id : str
    course_id : str
    section : int
    grade : str
