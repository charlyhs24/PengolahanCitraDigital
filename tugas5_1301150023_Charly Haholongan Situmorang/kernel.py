from tkinter import * #Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL # Install Using PIP
from PIL import ImageTk, Image
import matplotlib.mlab as mlab
import math
from skimage import exposure
from skimage import io, color


def convolusi(image,kernel):
    new_kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)   
    # for i in range (10):
    #     for j in range(10):
    #         print(output[i,j])
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    print(output.shape)
    print(image_padded.shape)
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):     # Loop over every pixel of the image
        for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).sum()        
    return output

image = cv2.imread("lol.png")
img = color.rgb2gray(image) 
image_equalized = exposure.equalize_adapthist(img/np.max(np.abs(img)), clip_limit=0.03)
# plt.imshow(image_equalized, cmap=plt.cm.gray)
# plt.axis('off')
# plt.show()
kernel_blur = np.array([[1,1,1],[1,1,1],[1,1,1]])
kernel_sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
image_blur = convolusi(img,kernel_sharp)
plt.imshow(image_blur, cmap=plt.cm.gray)
plt.axis('off')
plt.show()


# print(kernel_sharp[2])
        

