import streamlit as st
import requests
from PIL import Image
import os
# from model import model_nlp, encoder, model_cv
# import tensorflow as tf


URL = "http://host.docker.internal:8000"

# model = keras.models.load_model('path/to/location')
cv_labels = ['Baby_Care',
'Beauty_and_Personal_Care',
'Computers',
'Home_Decor_&_Festive_Needs',
'Home_Furnishing',
'Kitchen_&_Dining',
'Watches']

def predict(description):
    # load image
    file = {'file': ("newimage.png", open("newimage.png", 'rb'))}

    # request API to make prediction 
    response = requests.post(
        f"{URL}/upload_file",
        files=file,
        data={"description":description}
    )

    #remove images in directory
    # os.remove(f"{uploaded_file.name}")
    for file in os.listdir() :
        if file.endswith(('.png', ".jpg", ".jpeg", ".webp", ".JPG", ".JPEG")):
            os.remove(file) 
    
    return response.json()

# st.write(requests.get(URL).json())

st.title("Product category")

st.write("This is a simple chat bot to predict your product category with your description")

# container_nlp = st.container()
# form_prediction = container_nlp.form(key = 'prediction_nlp', clear_on_submit=True)

# description = form_prediction.text_input("Enter the name of the product")

# submit = form_prediction.form_submit_button("Submit")
# if submit:
    # result = model_nlp.predict([description]).argmax()
    # result = encoder.inverse_transform([result])
    # form_prediction.write(result[0])
# if st.checkbox("Show some data"):
#   data = [1, 2, 3, 4, 5]
#   st.write(data)

# container_cv = st.container()

# form_prediction_cv = container_cv.form(key = 'prediction_cv', clear_on_submit=True)

# file = form_prediction_cv.file_uploader('Your image', type=['jpeg', 'png', 'jpg', 'gif'] )

# submit_cv = form_prediction_cv.form_submit_button("Submit")
# if submit_cv:
#     image = file
    # img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
    # img_array = tf.keras.preprocessing.image.img_to_array(img)
    # img_array = tf.expand_dims(img_array, 0) 
    # predictions = model_cv.predict(img_array).argmax()
    # form_prediction_cv.write(cv_labels[predictions])
    # result = model_cv.predict([description]).argmax()
    # result = encoder.inverse_transform([result])
    # st.write(result)
# if st.checkbox("Show some data"):
#   data = [1, 2, 3, 4, 5]
#   st.write(data)

container_cv_nlp = st.container()


form_prediction= container_cv_nlp.form(key = 'prediction', clear_on_submit=True)
description = form_prediction.text_input("Enter the name of the product")
file = form_prediction.file_uploader('Your image', type=['jpeg', 'png', 'jpg', 'gif'] )

submit = form_prediction.form_submit_button("Submit")


if submit:

    # st.write(description)

    if file :
        img = Image.open(file)
        st.image(img)
        with open(file.name,"wb") as f:
            f.write(file.getbuffer())
            # resize image
            image = Image.open(file.name)
            image = image.resize((500,500),Image.ANTIALIAS)
            image.save(fp="newimage.png")

    st.write(predict(description))

