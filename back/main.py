import uvicorn
from fastapi import FastAPI, File, UploadFile

# import os
# import pathlib

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
# from io import BytesIO

app = FastAPI()

model = tf.keras.models.load_model("my_model.h5", custom_objects={'KerasLayer':hub.KerasLayer})

@app.get("/")
async def root():
    return {"message": "Welcome to the API !"}



@app.post("/upload_file")
async def read_root(file: UploadFile = File(...)):
 
    image = file.file._file

    #classes 
    classes = ['Baby_Care', 'Beauty_And_Personal_Care', 'Computers', 'Home_Decor_&_Festive_Needs', 'Home_Furnishing', 'Kitchen_&_Dining', 'Watches']

    #PREDICTION
    img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 

    predictions = model.predict(img_array)

    return {"info": f"file '{file.filename}'",
            "label":classes[np.argmax(predictions)],
            "confidence": f"{np.round(predictions[0][np.argmax(predictions)]*100, 2)}"
           }


if __name__ == "__main__":
    uvicorn.run("main:app")