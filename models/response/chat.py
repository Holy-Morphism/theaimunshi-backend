from pydantic_core import DatetimeSchema
from pydantic import BaseModel

class Message(BaseModel):
    timestamp:int
    message:content
    


