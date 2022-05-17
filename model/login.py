from pydantic import BaseModel, Field
from typing import Optional


class LoginModel(BaseModel):
    username: str
    password: str
    role: Optional[str] = 'user'
