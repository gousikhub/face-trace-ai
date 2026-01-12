from fastapi import FastAPI
from backend.face_engine import compare_faces
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/")
def home():
    return {"status": "Face Trace AI backend running"}

@app.get("/compare")
def compare():
    img1 = os.path.join(BASE_DIR, "dataset", "known", "person1.jpg")
    img2 = os.path.join(BASE_DIR, "dataset", "test", "unknown.jpg")

    return compare_faces(img1, img2)
