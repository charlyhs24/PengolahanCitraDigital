import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("DATASET/5.png")
threshold = image.copy()
imgToGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# hist = cv2.calcHist([imgToGray],[0],None,[256],[0,256])``
print(threshold.shape[0])
for x in range(imgToGray.shape[0]):
    for y in range(imgToGray.shape[1]):
        if(imgToGray[x,y] < 60):
            threshold[x,y] = 0
        else:
            threshold[x,y] = 255
# plt.hist(imgToGray.ravel(),256,[0,256])
# plt.show()
# cv2.imshow('Original image',image)
# cv2.imshow('Gray image', threshold)
cv2.imwrite("5.png", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()