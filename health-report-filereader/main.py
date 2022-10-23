import io

from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse

import numpy as np
import easyocr
from easyocr import Reader
import argparse
import cv2
app = FastAPI()


@app.get('/')
async def root():
     return {'status': 'ok'}


@app.post('/style')
async def predict(img_bytes: bytes = File(...)):
     img = io.BytesIO(img_bytes)
     img.seek(0)
     return StreamingResponse(
         img,
         media_type="image/jpg",
    )

@app.post('/file')
async def create_upload_file(file: UploadFile):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    image = cv2.imread(f"./files/${filename}")
    # OCR the input image using EasyOCR
    print("[INFO] OCR'ing input image...")
    reader = Reader(["pt"], gpu=False)
    results = reader.readtext(image)

    return {"results": results}