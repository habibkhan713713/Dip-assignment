#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
image = cv2.imread('tree.jpg')
new_dimensions = (250, 250)  # Adjust these values according to your needs
resized_image = cv2.resize(image, new_dimensions)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
rgb_image = cv2.imread('coin.png')
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
rgb_image = cv2.imread('coin.png')
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.medianBlur(gray_image,15) 
_, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


import cv2
import numpy as np
arr = np.full((493, 756 , 3), 255 ,dtype = np.uint8)
segmented = np.full((493, 756 , 3), 0 ,dtype = np.uint8)
rgb_image = cv2.imread('coin.png')
rgb_copy = cv2.imread('coin.png')
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.medianBlur(gray_image,15) 
_, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)

for i in range(binary_image.shape[0]):
    for j in range(binary_image.shape[1]-1):
        if((binary_image[i,j] == 255 and binary_image[i,j+1] == 0 ) or (binary_image[i,j] == 0 and binary_image[i,j+1] == 255 )) :
             arr[i, j:j+2, 1:3 ] =  0
for i in range(binary_image.shape[1]):
    for j in range(binary_image.shape[0]-1):
        if((binary_image[j,i] == 255 and binary_image[j+1,i] == 0 ) or (binary_image[j,i] == 0 and binary_image[j+1,i] == 255 )) :
             arr[j:j+2, i, 1:3 ] =  0
for i in range(binary_image.shape[0]):
    for j in range(binary_image.shape[1]-1):
        if arr[i,j,1] == 0 :
             rgb_image[i, j,1:3] =  [0,0]
             rgb_image[i, j,2] =  255
for i in range(binary_image.shape[0]):
    for j in range(binary_image.shape[1]-1):
        if binary_image[i,j] == 0 :
             segmented[i, j,:] =  rgb_copy[i,j,:] 
binary_image = cv2.bitwise_not(binary_image)                
print("Number of Coins in image : " , len(contours))
cv2.imshow('Segmented Image', segmented)
cv2.imshow('Highlighted Image', rgb_image)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.waitKey(0) 
cv2.destroyAllWindows()

