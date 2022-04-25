from fastapi import APIRouter
from database import session
from base_model import Base_Student
import models

router = APIRouter(
    prefix="/student",
    tags=["Student"],
    responses={404: {"description": "Not found"}},
)


@router.get('/') # List all students
async def get_all_std():
    std_all = session.query(models.Student)
    a_list = list()
    for i in std_all:
        a_list.append({
            "std_id" : i.std_id,
            "gov_id" : i.gov_id,
            "name" : i.name,
            "surname" : i.surname,
            "major" : i.major,
            "department": i.department
        })
    return a_list

@router.get('/find_student/{student_id}') # Find one Student
async def find_student(student_id:str):
    std_one = session.query(models.Student).filter(models.Student.std_id==student_id).first()
    return std_one

@router.post('/add_student') # Add Student
async def add_student(item: Base_Student):
    std_data = models.Student(
        std_id = item.student_id,
        gov_id = item.gov_id,
        name = item.name,
        surname = item.surname,
        major = item.major,
        department = item.department
    )
    session.add(std_data)
    session.commit()
    return {
        "message" : "add successfully."
    }

@router.put('/update_student/{student_id}') # Update Student
async def update_student(student_id:str, item:Base_Student):
    std_one = session.query(models.Student).filter(models.Student.std_id==student_id).first()
    std_one.gov_id = item.gov_id
    std_one.name = item.name
    std_one.surname = item.surname
    std_one.major = item.major
    std_one.department = item.department

    session.commit()

    return std_one

@router.delete('/delete_student/{student_id}') # Delete Student
async def delete_student(student_id:str):
    std_one = session.query(models.Student).filter(models.Student.std_id==student_id).first()

    session.delete(std_one)
    session.commit()

    return std_one