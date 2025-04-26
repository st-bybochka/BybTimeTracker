
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int
    name: Annotated[str, Field(None, max_length=30, min_length=3)]
    last_name: Annotated[str, Field(None, max_length=30, min_length=3)]
    created_at: datetime
    updated_at: datetime
