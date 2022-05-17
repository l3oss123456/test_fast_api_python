from database import db
from bson.objectid import ObjectId


def employee_query(id=""):
    try:
        _results = []
        if id == "" and id != None:
            results = list(db.employees.find())

            for row in results:
                _results.append({
                    '_id': str(row['_id']),
                    'name': row['name'],
                    'lname': row['lname'],
                })
        else:
            results = list(db.employees.find(
                {"_id": ObjectId(id)}))

            for row in results:
                _results.append({
                    '_id': str(row['_id']),
                    'name': row['name'],
                    'lname': row['lname'],
                })

        return _results

    except:
        return 'error query from employees database'
