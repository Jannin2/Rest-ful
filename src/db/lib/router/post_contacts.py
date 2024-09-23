from src.db.lib.managedb import ManageDb


def post_contacts(new_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    new_contact = new_contact.dict()
    contacts.append(new_contact)
    md.write_contacts(contacts)
    return {
        "success" : True,
        "message" : "Added new Contact"
    }
    