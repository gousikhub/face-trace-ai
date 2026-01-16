from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import uuid

from backend.face_engine import compare_faces

# ✅ Create FastAPI app
app = FastAPI(title="Face Trace AI")

# ✅ Enable CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (OK for dev / hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Temp upload folder
UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ✅ Health check
@app.get("/")
def home():
    return {"status": "Face Trace AI backend running"}

# ✅ Face comparison endpoint
@app.post("/compare")
def compare(
    known: UploadFile = File(...),
    unknown: UploadFile = File(...)
):
    known_path = os.path.join(UPLOAD_DIR, f"known_{uuid.uuid4()}.jpg")
    unknown_path = os.path.join(UPLOAD_DIR, f"unknown_{uuid.uuid4()}.jpg")

    try:
        # Save uploaded files
        with open(known_path, "wb") as f:
            shutil.copyfileobj(known.file, f)

        with open(unknown_path, "wb") as f:
            shutil.copyfileobj(unknown.file, f)

        # Compare faces
        result = compare_faces(known_path, unknown_path)

        return {
            **result,
            "message": "Face comparison completed"
        }

    finally:
        # Cleanup temp files
        if os.path.exists(known_path):
            os.remove(known_path)
        if os.path.exists(unknown_path):
            os.remove(unknown_path)
