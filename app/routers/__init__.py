from fastapi import APIRouter

welcome = APIRouter()


@welcome.get("/", include_in_schema=False)
async def start_welcome():
    return "Welcome to the MaisTodos."
