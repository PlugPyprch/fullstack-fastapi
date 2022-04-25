from fastapi import APIRouter
from database import session
from base_model import Base_Department
import models

router = APIRouter(
    prefix="/department",
    tags=["Department"],
    responses={404: {"description": "Not found"}},
)

@router.get('/') # List all Department
async def get_all_department():
    department_all = session.query(models.Department)
    a_list = list()
    for i in department_all:
        a_list.append({
            "department_id" : i.department_id,
            "name" : i.name
        })
    return a_list

@router.get('/find_department/{department_id}') # Find one Department
async def find_department(department_id:str):
    department_one = session.query(models.Department).filter(models.Department.department_id==department_id).first()
    return department_one

@router.post('/add_department') # Add Department
async def add_department(item: Base_Department):
    department_data = models.Department(
        department_id = item.department_id,
        name = item.name
    )
    session.add(department_data)
    session.commit()
    return {
        "message" : "add successfully."
    }

@router.put('/update_department/{department_id}') # Update Department
async def update_department(department_id:str, item:Base_Department):
    department_one = session.query(models.Department).filter(models.Department.department_id==department_id).first()
    department_one.name = item.name

    session.commit()
    return department_one

@router.delete('/delete_department/{department_id}') # Delete Department
async def delete_department(department_id:str):
    department_one = session.query(models.Department).filter(models.Department.department_id==department_id).first()

    session.delete(department_one)
    session.commit()

    return department_one