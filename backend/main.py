# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from teacher_api import router as teacher_router

app = FastAPI(title="ClassSight - Teacher API")

# CORS for local development - restrict in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teacher_router)

@app.get("/")
def root():
    return {"message": "Teacher API running!"}
