from fastapi import APIRouter, Body
from app.domain.auth.auth_handler import signJWT
from app.domain.auth.schema import UserLoginSchema

router = APIRouter()


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    return signJWT(user.email)
