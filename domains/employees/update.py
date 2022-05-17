from database import db
from bson.objectid import ObjectId


# def employee_update(args=None):
#     try:
#         if args != None:
#             name = args['name']
#             lname = args['lname']
#             _id = args['id']

#             result = db.employees.update_one({"_id": ObjectId(_id)}, {
#                 "$set": {
#                     "name": name,
#                     "lname": lname
#                 }
#             })

#             return 'Update Successful!'
#         else:
#             return 'args is missing!'
#     except:
#         return 'error query from employees database'

def employee_update(args=None):
    try:
        if args != None:
            name = args['name']
            lname = args['lname']
            _id = args['id']

            result = db.employees.update_one({"_id": ObjectId(_id)}, {
                "$set": {
                    "name": name,
                    "lname": lname
                }
            })

            return 'Update Successful!'
        else:
            return 'args is missing!'
    except:
        return 'error query from employees database'
