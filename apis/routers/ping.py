from fastapi import APIRouter
from appconf import API_ID, API_VERSION, logger

router = APIRouter(
    prefix="/ping",
    tags=["ping"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def pong():
  logger.info(f"Ping and Pong {API_VERSION}")
  return {"message": "pong", "appid": API_ID, "version": API_VERSION }
