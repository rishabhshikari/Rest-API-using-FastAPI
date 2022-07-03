from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import json


app = FastAPI()

class Users(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open('User.json','r') as f:
    User = json.load(f)['User']

@app.get('/User/{u_id}')
def get_user(u_id : int):
    person = [p for p in User if p['id'] == u_id]
    return person[0] if len(person) > 0 else{}


@app.get('/search')
def search_user(gender: Optional[str] = Query(None, tile="Gender", description="The Gender to Search for"),
                name: Optional[str] = Query(None, title="Name", description="The Name to Search for")):
    people1 = [p for p in User if gender in p['gender']]
    if name is None:
        if gender is None:
            return User
        else:
            return people1
    else:
        people2 = [p for p in User if name.lower() in p['name'].lower()]
        if gender is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined
@app.get("/User_List")
async def fetch_users():
    return User



