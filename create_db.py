from database import Base, engine
from models import Student, Course, Major, Department, Enroll

Base.metadata.create_all(engine)

