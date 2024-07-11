from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
    tags=["ping"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def pong():
  return {"message": "pong"}
