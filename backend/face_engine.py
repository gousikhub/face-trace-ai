from deepface import DeepFace
import os

def compare_faces(img1_path, img2_path):
    # Check file existence first
    if not os.path.exists(img1_path):
        return {"error": f"Image not found: {img1_path}"}

    if not os.path.exists(img2_path):
        return {"error": f"Image not found: {img2_path}"}

    try:
        result = DeepFace.verify(
            img1_path=img1_path,
            img2_path=img2_path,
            model_name="VGG-Face",
            detector_backend="opencv",
            enforce_detection=False  
        )

        return {
            "verified": result.get("verified"),
            "distance": round(result.get("distance", 0), 4),
            "threshold": result.get("threshold"),
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
