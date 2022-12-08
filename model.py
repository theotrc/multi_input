from tensorflow import keras
import pickle 
import tensorflow_hub as hub


model_cv = keras.models.load_model('models/my_model.h5', custom_objects={'KerasLayer':hub.KerasLayer})



model_nlp = keras.models.load_model('models/model_1_nlp')

file = open('le.pickle', 'rb')

# dump information to that file
encoder = pickle.load(file)