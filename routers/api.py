from fastapi import APIRouter
from endpoints import employee,login

router = APIRouter()
router.include_router(login.router)
router.include_router(employee.router)
