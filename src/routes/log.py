from fastapi import APIRouter
from starlette.status import (
    HTTP_201_CREATED, 
    HTTP_500_INTERNAL_SERVER_ERROR)

from src.models import NewRegister
from src.use_cases import Log
from src.utils import UJSONResponse, LogMessage


log_routes = APIRouter(tags=['Log'])

@log_routes.post('/log')
def create_log(log: NewRegister):
    try:
        Log.create_register(log)
        return UJSONResponse(LogMessage.create,HTTP_201_CREATED)
    except Exception as error:
        return UJSONResponse(
            LogMessage.error,
            HTTP_500_INTERNAL_SERVER_ERROR)