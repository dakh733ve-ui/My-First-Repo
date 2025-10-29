from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
import uuid
import os
import cv2
from random import randint
from fastapi.responses import FileResponse

IMAGEDIR = "images/"
CASCADEDIR = "cascades/"

app = FastAPI()

# Load Haar cascades
#face_cascade = cv2.CascadeClassifier(f"{CASCADEDIR}haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier(f"{CASCADEDIR}haarcascade_eye.xml")
#body_cascade = cv2.CascadeClassifier(f"{CASCADEDIR}haarcascade_fullbody.xml")


@app.get("/")
def index():
    return {"Message": "Hello World"}


@app.get("/Hello")
def get_name(name: str):
    return {"Welcome to my first repo": f"{name}"}

@app.post("/upload")
async def create_uplaod_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    
    save_path = f"{IMAGEDIR}{file.filename}" 
    with open(save_path, "wb") as f:
        f.write(contents)
    
    has_face = detect_face(save_path)

    
    return FileResponse(
        path=save_path,
        media_type="image/jpeg",
        filename=file.filename,
        headers={"face_detected": str(has_face)}
    )

#@app.get("/show/")
#async def read_random_file():
#    files = os.listdir(IMAGEDIR)
#    random_index = randint(0, len(files) - 1)
#    path = f"{IMAGEDIR}{files[random_index]}"

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.118.223", port=57577, reload=True)

print(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


import cv2

def detect_face(image_path: str):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles on detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the labeled image back
    cv2.imwrite(image_path, img)

    # Return True if any faces detected
    return len(faces) > 0
