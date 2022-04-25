from fastapi import APIRouter
from database import session
from base_model import Base_Major
import models

router = APIRouter(
    prefix="/major",
    tags=["Major"],
    responses={404: {"description": "Not found"}},
)

@router.get('/') # List all majors
async def get_all_major():
    major_all = session.query(models.Major)
    a_list = list()
    for i in major_all:
        a_list.append({
            "major_id" : i.major_id,
            "name" : i.name
        })
    return a_list

@router.get('/find_major/{major_id}') # Find one Major
async def find_major(major_id:str):
    major_one = session.query(models.Major).filter(models.Major.major_id==major_id).first()
    return major_one

@router.post('/add_major') # Add Major
async def add_major(item: Base_Major):
    major_data = models.Major(
        major_id = item.major_id,
        name = item.name
    )
    session.add(major_data)
    session.commit()
    return {
        "message" : "add successfully."
    }

@router.put('/update_major/{major_id}') # Update Major
async def update_major(major_id:str, item:Base_Major):
    major_one = session.query(models.Major).filter(models.Major.major_id==major_id).first()
    major_one.name = item.name

    session.commit()
    return major_one

@router.delete('/delete_major/{major_id}') # Delete Major
async def delete_major(major_id:str):
    major_one = session.query(models.Major).filter(models.Major.major_id==major_id).first()

    session.delete(major_one)
    session.commit()

    return major_one