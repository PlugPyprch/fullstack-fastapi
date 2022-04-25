from fastapi import APIRouter
from database import session
from base_model import Base_Course
import models

router = APIRouter(
    prefix="/course",
    tags=["Course"],
    responses={404: {"description": "Not found"}},
)

@router.get('/') # List all courses
async def get_all_course():
    couse_all = session.query(models.Course)
    a_list = list()
    for i in couse_all:
        a_list.append({
            "course_id" : i.course_id,
            "name" : i.name,
            "section" : i.section,
            "credit" : i.credit,
            "str_time" : i.str_time,
            "end_time": i.end_time
        })
    return a_list

@router.get('/find_course/{course_id}') # Find one Course
async def find_course(course_id:str):
    course_one = session.query(models.Course).filter(models.Course.course_id==course_id).first()
    return course_one

@router.post('/add_course') # Add Course
async def add_course(item: Base_Course):
    course_data = models.Course(
        course_id = item.course_id,
        name = item.name,
        section = item.section,
        credit = item.credit,
        str_time = item.str_time,
        end_time = item.end_time
    )
    session.add(course_data)
    session.commit()
    return {
        "message" : "add successfully."
    }

@router.put('/update_course/{course_id}') # Update Course
async def update_course(course_id:str, item:Base_Course):
    course_one = session.query(models.Course).filter(models.Course.course_id==course_id).first()
    course_one.name = item.name
    course_one.section = item.section
    course_one.credit = item.credit
    course_one.str_time = item.str_time
    course_one.end_time = item.end_time

    session.commit()

    return course_one

@router.delete('/delete_course/{course_id}') # Delete Course
async def delete_course(course_id:str):
    course_one = session.query(models.Course).filter(models.Course.course_id==course_id).first()

    session.delete(course_one)
    session.commit()

    return course_one