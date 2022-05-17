from fastapi import APIRouter
# from fastapi import Query
from model.employee import EmployeeModel
from typing import Optional
# from pydantic import BaseModel
from domains.employees.query import employee_query
from domains.employees.insert import employee_insert
from domains.employees.update import employee_update
from domains.employees.delete import employee_delete

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/employee",
    # tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_all_employees():
    resp = employee_query()
    return resp


@router.get("/{id}")
def get_employee(id: Optional[str] = ""):
    resp = employee_query(id)
    return resp


@router.post("/insert")
def insert_employee(info: EmployeeModel):
    resp = employee_insert({
        "name": info.name,
        "lname": info.lname
    })
    return resp


@router.put("/update/{id}")
def update_employee(info: EmployeeModel, id: Optional[str] = ""):
    resp = employee_update({
        "id": id,
        "name": info.name,
        "lname": info.lname
    })
    return resp


@router.delete("/delete/{id}")
def delete_employee(id: Optional[str] = ""):
    # print('idididid;', id)
    resp = employee_delete(id)
    return resp


# @router.post('/login')
# def login(user: User):
#     return {"user": user}
