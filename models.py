from database import Base
from sqlalchemy import String,Integer,Column


class Product(Base):
#ต้องใช้__xxx__ เสมอ
              __tablename__ ='productxx'
              product_id=Column(Integer,primary_key=True)
              product_name=Column(String(255),nullable=False)
              description=Column(String(255),nullable=False)
              price=Column(Integer)
              status=Column(String(255))

              def __repr__(self):
                            return f"<Product product_name={self.product_name} description={self.description}>"


class User(Base):
              __tablename__ = 'member'
              user_id=Column(Integer,primary_key=True)
              username=Column(String(50))
              password=Column(String(50))
              age=Column(Integer)
              email=Column(String(50))

              def __repr__(self):
                            return f"<User username={self.username} password={self.password}>"
