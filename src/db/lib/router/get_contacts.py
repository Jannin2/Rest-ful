from src.db.lib.managedb import ManageDb

def get_contacts():
    md = ManageDb()
    return md.read_contacts()
