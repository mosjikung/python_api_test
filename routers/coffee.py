from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
              prefix="/coffee",
              tags=['Coffee'],
              responses ={404:{
                            'message' : "Not found"
              }}
              
)


class Coffee(BaseModel):
    name:str
    description: Optional[str] = None
    price:float
    star : int

coffee_db = [
{
    'name' : 'Espresso',
    'description' : 'เป็นกาแฟดำที่เข้มที่สุด',
    'price' : 61,
    'star'  : 5
},
{
    'name' : 'Americano',
    'description' : 'เป็นกาแฟดำ ที่ใส่แค่ 1 shot ตามด้วยน้ำร้อน',
    'price' : 55,
    'star'  : 5
}
]

@router.get("/")
def read_root():
    return coffee_db

@router.get("/coffee/{id}")
def coffee_by_id(id:int):
    coffee = coffee_db[id-1]
    return coffee

#จะใช้ModelBaseของCoffee Class
@router.post('/coffee')
def create_coffee(coffee: Coffee):
    coffee = coffee_db.append(coffee)
    return coffee_db[-1]

@router.delete('/coffee/{id}')
def delete_coffee(id:int):
    coffee = coffee_db[id-1]
    coffee_db.pop(id-1)
    result = {'msg',f"{coffee['name']} was Delete!"}
    return result

@router.put('/coffee/{id}')
def update_coffee(id:int, coffee:Coffee):
    coffee_db[id-1].update(**coffee.dict())
    result ={'msg': f"Coffee id {id} Update successful!!"}
    return result