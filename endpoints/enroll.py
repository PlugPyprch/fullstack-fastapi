from fastapi import APIRouter
from database import session
from base_model import Base_Enroll
import models

router = APIRouter(
    prefix="/enroll",
    tags=["Enroll"],
    responses={404: {"description": "Not found"}},
)

@router.get('/') # List all enrolls
async def get_all_enroll():
    enroll_all = session.query(models.Enroll)
    a_list = list()
    for i in enroll_all:
        a_list.append({
            "enroll_id" : i.enroll_id,
            "std_id" : i.std_id,
            "course_id" : i.course_id,
            "section" : i.section,
            "grade": i.grade
        })
    return a_list

@router.get('/find_enroll/{enroll_id}') # Find one Enroll
async def find_enroll(enroll_id:str):
    enroll_one = session.query(models.Enroll).filter(models.Enroll.enroll_id==enroll_id).first()
    return enroll_one

@router.post('/add_enroll') # Add Enroll
async def add_enroll(item: Base_Enroll):
    enroll_data = models.Enroll(
        #enroll_id = item.enroll_id,
        std_id = item.std_id,
        course_id = item.course_id,
        section = item.section,
        grade = item.grade
    )
    session.add(enroll_data)
    session.commit()
    return {
        "message" : "add successfully."
    }

@router.put('/update_enroll/{enroll_id}') # Update Enroll
async def update_enroll(enroll_id:str, item:Base_Enroll):
    enroll_one = session.query(models.Enroll).filter(models.Enroll.enroll_id==enroll_id).first()
    enroll_one.std_id = item.std_id
    enroll_one.course_id = item.course_id
    enroll_one.section = item.section
    enroll_one.grade = item.grade

    session.commit()

    return enroll_one

@router.delete('/delete_enroll/{enroll_id}') # Delete Enroll
async def delete_enroll(enroll_id:str):
    enroll_one = session.query(models.Enroll).filter(models.Enroll.enroll_id==enroll_id).first()

    session.delete(enroll_one)
    session.commit()

    return enroll_one