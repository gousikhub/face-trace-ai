from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import os
import shutil
import uuid

from backend.face_engine import compare_faces

# ✅ THIS LINE WAS MISSING OR MISPLACED
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all frontend origins (dev only)
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"status": "Face Trace AI backend running"}

@app.post("/compare")
def compare(
    known: UploadFile = File(...),
    unknown: UploadFile = File(...)
):
    known_path = os.path.join(UPLOAD_DIR, f"known_{uuid.uuid4()}.jpg")
    unknown_path = os.path.join(UPLOAD_DIR, f"unknown_{uuid.uuid4()}.jpg")

    with open(known_path, "wb") as f:
        shutil.copyfileobj(known.file, f)

    with open(unknown_path, "wb") as f:
        shutil.copyfileobj(unknown.file, f)

    result = compare_faces(known_path, unknown_path)

    os.remove(known_path)
    os.remove(unknown_path)

    return result
