from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

update_postgres = "postgresql://ubrxoivxlgfvtu:c3b4ddff2e06f2d663497e9d943d3d1d4519f5c9ebf3c9419a39229a22559882@ec2-52-3-2-245.compute-1.amazonaws.com:5432/d2o4u9p0kg8pgj"
heroku_postgres = "postgresql://odrcjrtkccygxm:9e9355464d374f10e680fa5b07df2d8841d6b89088f3f6c6169ce721a2d45d2b@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d50nqb5br2s4uv"

heroku_postgres = update_postgres

engine = create_engine(heroku_postgres)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()