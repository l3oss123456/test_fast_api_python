from database import db


def employee_insert(args=None):
    try:
        if args != None:
            name = args['name']
            lname = args['lname']

            result = db.employees.insert_one({"name": name, "lname": lname})

            return 'Insert Successful!'
        else:
            return 'args is missing!'

    except:
        return 'error query from employees database'
