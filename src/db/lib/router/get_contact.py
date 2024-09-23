from src.db.lib.managedb import ManageDb
from fastapi import HTTPException


def get_contact(id_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
        
    raise HTTPException(status_code=404, detail="Contact not found") 
    