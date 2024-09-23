from src.db.lib.managedb import ManageDb
from fastapi import HTTPException


def delete_contact(id_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)
            
            md.write_contacts(contacts)
            
            return {
                "succes" : True,
                "message" : "Deleted contact"
            }
            
    raise HTTPException(status_code= 404, detail= "contact not found")