from database import Base,engine
from models import Product

print("Create Database ...")

Base.metadata.create_all(engine) #createdb