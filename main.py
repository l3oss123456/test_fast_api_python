from distutils.log import info
from optparse import Option
from typing import Optional
from fastapi import FastAPI, Request, APIRouter
from pydantic import BaseModel
import time
import uvicorn
from domains.employees.query import employee_query
from domains.employees.insert import employee_insert
from domains.employees.update import employee_update
from domains.employees.delete import employee_delete
from routers.api import router as api_router

app = FastAPI()
# app = APIRouter()
# app.include_route(employees.router)
app.include_router(api_router)


# class User(BaseModel):
#     username: str
#     password: str
#     role: Optional[str] = 'user'


# class UserInfo(BaseModel):
#     name: str
#     lname: str


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
