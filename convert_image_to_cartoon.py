'''To run give command:  python3 convert_image_to_cartoon.py  input_pic_name.jpg  output_pic_name.jpg'''

import cv2
import numpy as np
import sys


#reading the image file
def read_file(filename):
	img = cv2.imread(filename)
	#cv2.imshow('image' , img)
	#cv2.waitKey(0)
	#cv2.destroyallwindows()
	return img

#Creating edge mask i.e outer border of image
def edge_mask(img , line_size , blur_value):
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	gray_blur = cv2.medianBlur(gray , blur_value)
	edges = cv2.adaptiveThreshold(gray_blur , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , line_size , blur_value)
	return edges


#Reducing colors of the Image
def color_quantization(img , k):
	data = np.float32(img).reshape((-1 , 3))
	
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER , 20 , 0.001)
	ret , label , center = cv2.kmeans(data , k , None , criteria , 10 , cv2.KMEANS_RANDOM_CENTERS)
	center = np.uint8(center)
	result = center[label.flatten()]
	result = result.reshape(img.shape)
	return result

img_file = str(sys.argv[1])
save_file = str(sys.argv[2])

print('Reading File')
img = read_file(img_file)

print('Creating Outline')
edges = edge_mask(img , 7 , 7)     #edge_mask(image , line_size , blur_value)

'''cv2.imshow('image' , edges)
cv2.waitKey(0)
cv2.destroyallwindows()'''

print('Creating cartoon Image')
img = color_quantization(img , 20)    #color_quantization(image , amount_of_colors_to_use)

'''cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyallwindows()'''


#reducing sharpness of image
print('Reducing Sharpness')
blurred = cv2.bilateralFilter(img , d = 7 , sigmaColor = 200 , sigmaSpace = 200)		#To give cartoonic effect

'''cv2.imshow('image' , blurred)
cv2.waitKey(0)
cv2.destroyallwindows()'''


print('Creating Final image')
cartoon = cv2.bitwise_and(blurred , blurred , mask = edges)			#Merging the outline and blurred image

'''cv2.imshow('image' , cartoon)
cv2.waitKey(0)
cv2.destroyallwindows()'''



cv2.imwrite(save_file , cartoon)
print('image saved to {}'.format(save_file))

