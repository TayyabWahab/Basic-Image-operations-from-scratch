#Wavlet Transform and Inverse wavelet transform using db9 method


from pywt import dwt2, idwt2
import cv2
import matplotlib.pyplot as plt
import numpy as np

def average_coff(c):

    for i in range(1,c.shape[0]-1):
        for j in range(1,c.shape[1]-1):
            c[i][j] = ((c[i-1][j-1]+c[i-1][j]+c[i-1][j+1])+(c[i][j-1]+c[i][j]+c[i][j+1])+(c[i+1][j-1]+c[i+1][j]+c[i+1][j+1]))/9
    return c


def display(image,Title = ''):
    plt.figure(figsize=(10,20))
    plt.imshow(img,cmap = 'gray')
    plt.title(Title)
    plt.show()

img = cv2.imread('image.jpg',0)
h,w = img.shape
img = img/255
cA, (cH, cV, cD) = dwt2(img, 'db9')  

cA = average_coff(cA)
cH = average_coff(cH)
cV = average_coff(cV)
cD = average_coff(cD)

result = idwt2((cA,(cH,cV,cD)),'db9')[:h,:w]


display(img,'Original Image')
display(result,'Resultant Image')
cv2.imwrite("Wavlet Results.jpg",result)


