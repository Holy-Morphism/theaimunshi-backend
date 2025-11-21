from pydantic import BaseModel, Field
from typing import Literal
import time

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: int