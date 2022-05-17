from database import db
from bson.objectid import ObjectId


# def employee_delete(args=None):
#     try:
#         if args != None:
#             _id = args['id']

#             result = db.employees.delete_one({"_id": ObjectId(_id)})

#             return 'Delete Successful!'
#         else:
#             return 'args is missing!'

#     except:
#         return 'error query from employees database'

def employee_delete(_id=None):
    try:
        if _id != None:
            # _id = args['id']

            result = db.employees.delete_one({"_id": ObjectId(_id)})

            return 'Delete Successful!'
        else:
            return 'args is missing!'

    except:
        return 'error query from employees database'
