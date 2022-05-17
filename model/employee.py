from pydantic import BaseModel
from typing import Optional


class EmployeeModel(BaseModel):
    name: str
    lname: str
