from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

update_postgres = "postgresql://odrcjrtkccygxm:9e9355464d374f10e680fa5b07df2d8841d6b89088f3f6c6169ce721a2d45d2b@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d50nqb5br2s4uv"
heroku_postgres = "postgresql://tlnjfkirfwhsgq:cea1945c190cda2fbc445e7e4c20642563d5438bc2ecf8fc60d9efa6a9860c74@ec2-34-192-210-139.compute-1.amazonaws.com:5432/dfttaot5g6t6o2"

heroku_postgres = update_postgres

engine = create_engine(heroku_postgres)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()