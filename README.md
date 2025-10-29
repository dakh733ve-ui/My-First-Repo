#Face Detection API using FastAPI & OpenCV

This is a simple web API built with **FastAPI** and **OpenCV** that lets you upload an image and automatically detects faces in it.

## What It Does

1. You can send an image to the `/upload` endpoint.
2. The API saves the image on the server.
3. It uses OpenCV to detect any faces in the image.
4. It draws rectangles around detected faces.
5. The API sends the labeled image back to you.
6. You can check the custom response header `face_detected` to see if a face was found (`True` or `False`).

## Requirements

You need to have Python installed (3.8 or newer).

Install the required packages:

pip install fastapi uvicorn opencv-python
