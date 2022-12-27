from keras.models import load_model
import numpy as np
from PIL import Image, ImageOps
#import matplotlib.pyplot as plt
# import cv2
import os.path
#import pickle
def leaf(path1, veggie):
  image = Image.open(path1)
  return (image_data(image), veggie.lower())

def image_data(image):
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  return normalized_image_array

mpath1 = './content/apple_model.h5'
mpath2 = './content/cherry_model.h5'
mpath3 = './content/corn_model.h5'
mpath4 = './content/bell_model.h5'
mpath5 = './content/potato_model.h5'
mpath6 = './content/strawberry_model.h5'
mpath7 = './content/tomato_model.h5'
path_gen = {"apple" : mpath1, "cherry" : mpath2, "corn" : mpath3, "pepper" : mpath4, "potato" : mpath5, "strawberry" : mpath6, "tomato" : mpath7}

mlist1 = {0:"Healthy", 1:"Apple Scab", 2:"Black Rot", 3:"Cedar Rust"}
mlist2 = {0:"Healthy", 1:"Powdery Mildew"}
mlist3 = {0:"Healthy", 2:"Northern Blight"}
mlist4 = {0:"Bacterial Spot", 1:"Healthy"}
mlist5 = {0:"Healthy", 1:"Early Blight", 2:"Late Blight"}
mlist6 = {0:"Healthy", 1:"Scorch"}
mlist7 = {0:"Healthy", 1:"Early Blight", 2:"Late Blight", 3:"Mosaic Virus"}
class_list = {"apple" : mlist1, "cherry" : mlist2, "corn" : mlist3,  "pepper" : mlist4, "potato" : mlist5, "strawberry" : mlist6, "tomato" : mlist7}

def matrix(img, veggie):
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  #data[0], veggie = leaf(input("image path : "), input("name : "))
  data[0], veggie = leaf(img, veggie)
  model = load_model(path_gen[veggie], compile=False)
  prediction = model.predict(data)
  readble_pred = np.around((prediction[0]*100),2)
  index = np.argmax(prediction[0])
  class_name = class_list[veggie]
  # print(readble_pred)
  my_pred = ""
  for i in range(0,len(readble_pred)):
    my_pred += f"The probability of {class_name[i]} is {str(readble_pred[i])[:4]}%\n"
  return my_pred

