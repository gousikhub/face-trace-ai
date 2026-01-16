from deepface import DeepFace

def compare_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(
            img1_path=img1_path,
            img2_path=img2_path,
            enforce_detection=True
        )

        return {
            "verified": result["verified"],
            "distance": round(result["distance"], 4),
            "threshold": result["threshold"],
            "status": "success"
        }

    except Exception:
        # Handles:
        # - No face detected
        # - Multiple faces
        # - Blurry / invalid images
        return {
            "verified": False,
            "distance": None,
            "threshold": None,
            "status": "face_not_detected"
        }
