import numpy as np
import keras
from keras.models import model_from_json
from keras.models import Sequential , Model
from keras.layers.core import Dense, Dropout, Activation, Flatten, Reshape
from keras.layers import Conv2D, MaxPooling2D, Input
from keras.optimizers import SGD, Adam
from keras.layers import concatenate #for concatenating tensors
import json
from PIL import Image
import tensorflow as tf

input_rows = 304
input_cols = 228
input_depth = 1
lamda = 0.5;
n = 100;

def loss_function(_true, _pred):
	_true = np.log(_true)
	_pred = np.log(_pred)
	first = np.subtract(_true, _pred)
	second = np.subtract(_pred, _true)
	first = np.square(first)
	f_sum = np.sum(first)
	s_sum = np.sum(second)
	s_sum = s_sum * s_sum;
	f_sum = f_sum/n
	s_sum = lamda * (s_sum/(n * n))
	return (f_sum - s_sum)


def Construct_Coarse_Model(input_rows, input_cols, input_depth=1):  #Functional API Construction
	
	input_image_coarse = Input(shape=(input_rows,input_cols,input_depth))
	
	Conv1_coarse = Conv2D(96,(11,11),strides=4)(input_image_coarse) #96 feature maps, 11*11 kernels, 4 stride
	MaxPool1_coarse = MaxPooling2D((2,2))(Conv1_coarse)

	Conv2_coarse = Conv2D(256,(5,5))(MaxPool1_coarse)
	MaxPool2_coarse = MaxPooling2D((2,2))(Conv2_coarse)

	Conv3_coarse = Conv2D(384,(3,3))(MaxPool2_coarse)
	
	Conv4_coarse = Conv2D(384,(3,3))(Conv3_coarse)

	Conv5_coarse = Conv2D(256,(3,3))(Conv4_coarse)

	Flatten = Flatten()(Conv5_coarse)

	Dense1_coarse = Dense(4096)(Flatten)
	Dense2_coarse = Dense(74*55)(Dense1_coarse)
	Reshape_coarse = Reshape((74,55,1))(Dense2_coarse)

	Coarse_model = Model(input_image_coarse,Reshape_coarse)

def Construct_Fine_Model(input_rows,input_cols,input_depth):
	#Fine Scale Model

	input_image_fine = Input(shape=(input_rows,input_cols,input_depth))
	feature_map_coarse = Input(shape=(74,55,1))

	Conv1_fine = Conv2D(63,(9,9),strides=2)(input_image_fine)
	MaxPool1_fine = MaxPooling2D((2,2))(Conv1_fine)

	Concatenate_1 = concatenate([MaxPool1_fine,feature_map_coarse])

	Conv2_fine = Conv2D(64,(5,5))(Concatenate_1)

	Conv3_fine = Conv2D(1,(5,5))(Conv2_fine)

	Fine_Model = Model([input_image_fine,feature_map_coarse],Conv3_fine)


# takes  the model, images and their labels as inputs
# saves the weights of the network in model.h5
# evaluates the final score of the training
def train(model, X_train, Y_train):
	model.fit(X_train, Y_train, batch_size=32, epochs=20)
	model.save_weights("model.h5", overwrite=True)
	with open("model.json", "w") as outfile:
		json.dump(model.to_json(), outfile)
	score = model.evaluate(X_train, Y_train)
	print("Score is {}\n".format(score))

# takes  the model as input
# and predicts the output for an image
def test(model, image)
	model.load_weights("model.h5")
	sgd = SGD(lr=0.01)
	model.compile(loss=loss_function, optimizer=sgd)
	#ima = path to an input image
	coarseOut = model.predict(image)
	#im = Image.fromarray(coarseOut)
	#img.save('outputs/myphoto.jpg', 'JPEG')
	return coarseOut

# processes an image before using it for training
# takes the path of  the image as input	 
def process_image(filename):
	im = Image.open(filename)
	im = im.convert('1') #convert the image to black and white
	im = im.resize((image_cols, image_rows), PIL.Image.ANTIALIAS) # resize the image
	im.load()
	data = np.asarray( im, dtype="int32")
	return data

# dummy function for creating the dataset after processing each image
def create_dataset(path)
	# definition of function to create dataset


























