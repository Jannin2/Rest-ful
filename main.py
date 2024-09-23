from fastapi import FastAPI, HTTPException
from src.db.lib.managedb import ManageDb

app = FastAPI()
md = ManageDb()

@app.get("/")
def root():
    return {"message": "Hi"}

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()
    
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
        
    raise HTTPException(status_code=404, detail="Contact not found")

@app.post("/api/contacts")
def add_contact(new_contact):
    pass
