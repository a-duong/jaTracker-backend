from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
import datetime
from datetime import date


class WorkType(str, Enum):
    onsite = "onsite"
    hybrid = "hybrid"
    remote = "remote"

class JobCreate(BaseModel):
    company: str
    role: str
    status: str = "Applied"
    location: Optional[str] = None
    job_url: Optional[str] = None
    notes: Optional[str] = None
    work_type: str = "hybrid"
    application_date: date = Field(default_factory=date.today)


class JobResponse(JobCreate):
    id: int

    class Config:
        from_attributes = True