from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uuid

from src.db.lib.router.get_contacts import get_contacts
from src.db.lib.router.get_contact import get_contact
from src.db.lib.router.post_contacts import post_contacts
from src.db.lib.router.put_contacts import put_contacts
from src.db.lib.router.delete_contact import delete_contact



class ContactModel(BaseModel):
    id : str = str(uuid())
    name : str
    phone : str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hi"}

@app.get("/api/contacts")
def get_all_contacts():
    return get_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    return get_contact(id_contact)

@app.post("/api/contacts")
def add_contact(new_contact: ContactModel):
   return post_contacts(new_contact)
    
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact: str, new_contact: ContactModel):
    return put_contacts(id_contact, new_contact)
    
@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact:str):
    return delete_contact(id_contact)


