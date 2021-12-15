from fastapi import BackgroundTasks, FastAPI
from starlette.status import HTTP_200_OK

from src.config import fastApiConfig
from src.db import MongoEngine
from src.models import NewRegister
from src.use_cases import CreateLog
from src.utils import LogMessage, UJSONResponse

app = FastAPI(**fastApiConfig)
db = MongoEngine().get_connection()


@app.post("/error")
def create_log_error(error: NewRegister, task: BackgroundTasks):
    task.add_task(CreateLog.handle, error)
    return UJSONResponse(LogMessage.created, HTTP_200_OK)
