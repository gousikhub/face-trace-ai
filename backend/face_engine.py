from deepface import DeepFace

def compare_faces(known_path: str, unknown_path: str):
    result = DeepFace.verify(
        img1_path=known_path,
        img2_path=unknown_path,
        model_name="VGG-Face",
        enforce_detection=True
    )

    return {
        "verified": result["verified"],
        "distance": result["distance"],
        "threshold": result["threshold"],
        "status": "success"
    }
