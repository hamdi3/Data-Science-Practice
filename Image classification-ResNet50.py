#using Keras Application "ResNet50" for Image classification und prediction

#Importing Keras libs
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

#importing numpy for Matrix operations
import numpy as np


model = ResNet50(weights='imagenet') #getting the model itself
img_path = r"path to image" #to define the image path

#importing matplotlib.pyplot for plotting the image
import matplotlib.pyplot as plt 
from skimage.io import imread #to turn an image into a matrix
#img = imread(img_path) # to save a matrix of the Picture


img = image.load_img(img_path, target_size=(224, 224)) #converting the image for processing
x = image.img_to_array(img) #to turn the image into an array for sake of comparing
x = np.expand_dims(x, axis=0)
x = preprocess_input(x) #running preprocessing 

preds = model.predict(x) #to get our predictions

print('Predicted:', decode_predictions(preds, top=3)[0]) # to print the Predictions, change the top Value for more Predictions
plt.imshow(img) #to show us the pic
