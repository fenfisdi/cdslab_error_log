from pydantic import BaseModel, Field

class NewRegister(BaseModel):
    aplication_name: str = Field(...)
    code: int = Field(...)
    message:str = Field(...)