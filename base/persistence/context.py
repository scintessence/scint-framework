from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from base.persistence import LifeCycle


class Context(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    lifecycle: LifeCycle
