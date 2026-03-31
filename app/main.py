from fastapi import FastAPI
from app.database import Base, engine
from app.routes import jobs

Base.metadata.create_all(bind=engine)

app = FastAPI(title="jaTracker API")

app.include_router(jobs.router)


@app.get("/")
def root():
    return {"message": "jaTracker is running"}