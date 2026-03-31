import datetime
from datetime import date
from sqlalchemy import Column, Integer, String, Text, Date
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, nullable=False, default="Applied")
    location = Column(String, nullable=True)
    work_type = Column(String, nullable=False, default="hybrid")
    application_date = Column(Date, nullable =False, default=datetime.date.today)
    job_url = Column(String, nullable=True)
    notes = Column(Text, nullable=True)