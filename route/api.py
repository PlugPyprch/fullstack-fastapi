from fastapi import APIRouter
from endpoints import student, course, major, department, enroll

router = APIRouter()
router.include_router(student.router)
router.include_router(course.router)
router.include_router(major.router)
router.include_router(department.router)
router.include_router(enroll.router)