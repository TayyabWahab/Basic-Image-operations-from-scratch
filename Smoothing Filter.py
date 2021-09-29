#Smoothing Filter of size 3x3, 7x7, 9x9 

import cv2
import numpy as np 
import matplotlib.pyplot as plt


def adding(image,i,j,size):
    temp = 0
    for k in range(j,j+size):
        temp = temp+image[i][k]
    return temp
    

def avg_filter(image,size):
    m, n = image.shape 
    filter_image = image
    for i in range(int(size/2), m-int(size/2)): 
        for j in range(int(size/2), n-int(size/2)):
            temp = 0
            if size == 3:
                temp = temp+adding(image,i-1,j-1,size)
                temp = temp+adding(image,i,j-1,size)
                temp = temp+adding(image,i+1,j-1,size)
                filter_image[i, j]= temp/9
            elif size == 7:
                
                temp = temp+adding(image,i-3,j-3,size)
                temp = temp+adding(image,i-2,j-3,size) 
                temp = temp+adding(image,i-1,j-3,size)
                temp = temp+adding(image,i,j-3,size)
                temp = temp+adding(image,i+1,j-3,size)
                temp = temp+adding(image,i+2,j-3,size)
                temp = temp+adding(image,i+3,j-3,size)
                filter_image[i, j]= temp/49
            elif size == 9:
                temp = temp+adding(image,i-4,j-4,size)
                temp = temp+adding(image,i-3,j-4,size)
                temp = temp+adding(image,i-2,j-4,size) 
                temp = temp+adding(image,i-1,j-4,size)
                temp = temp+adding(image,i,j-4,size)
                temp = temp+adding(image,i+1,j-4,size)
                temp = temp+adding(image,i+2,j-4,size)
                temp = temp+adding(image,i+3,j-4,size)
                temp = temp+adding(image,i+4,j-4,size)
                filter_image[i, j]= temp/81
              
    return filter_image

if __name__ == '__main__':

    img = cv2.imread('image.jpg',0)
    plt.imshow(img)
    plt.show()
    filtered_image = avg_filter(img,9)
    cv2.imwrite("Result_smoothing_9x9.jpg",filtered_image)

    plt.imshow(filtered_image)
    plt.show()