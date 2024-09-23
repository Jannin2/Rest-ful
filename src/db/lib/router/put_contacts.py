from src.db.lib.managedb import ManageDb
from fastapi import HTTPException



def put_contacts(id_contact, new_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if str(contact["id"]) == id_contact:  
            updated_contact = new_contact.dict()

            
            if new_contact.name == "":
                updated_contact["name"] = contact["name"]
                
            if new_contact.phone == "":
                updated_contact["phone"] = contact["phone"]

           
            contacts[index] = updated_contact
            
            
            md.write_contacts(contacts)
            
            return {
                "success": True,
                "message": "Contact updated successfully"
            }
    
    raise HTTPException(status_code=404, detail="Contact not found")
