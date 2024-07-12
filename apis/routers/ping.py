from fastapi import APIRouter
from configuration import API_ID, API_VERSION
router = APIRouter(
    prefix="/ping",
    tags=["ping"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def pong():
  return {"message": "pong", "appid": API_ID, "version": API_VERSION }
