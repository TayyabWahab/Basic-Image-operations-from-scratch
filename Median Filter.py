#Median Filter of size 3x3, 7x7, 9x9

import cv2
import numpy as np 
import matplotlib.pyplot as plt


def get_values(image,i,j,size):
    temp = []
    for k in range(j,j+size):
        temp.append(image[i][k])
    return temp
    

def find_median(image,size):
    m, n = image.shape 
    filter_image = image
    print(int(size/2),m-int(size/2),n-int(size/2))
    for i in range(int(size/2), m-int(size/2)): 
        for j in range(int(size/2), n-int(size/2)):
            temp = []
            if size == 3:
                temp = temp+get_values(image,i-1,j-1,size)
                temp = temp+get_values(image,i,j-1,size)
                temp = temp+get_values(image,i+1,j-1,size)
                temp = np.sort(temp)
                med = np.median(temp)
                filter_image[i, j]= int(med)
            elif size == 7:
                
                temp = temp+get_values(image,i-3,j-3,size)
                temp = temp+get_values(image,i-2,j-3,size) 
                temp = temp+get_values(image,i-1,j-3,size)
                temp = temp+get_values(image,i,j-3,size)
                temp = temp+get_values(image,i+1,j-3,size)
                temp = temp+get_values(image,i+2,j-3,size)
                temp = temp+get_values(image,i+3,j-3,size)
                med = np.median(temp)
                filter_image[i, j]= int(med)
            elif size == 9:
                temp = temp+get_values(image,i-4,j-4,size)
                temp = temp+get_values(image,i-3,j-4,size)
                temp = temp+get_values(image,i-2,j-4,size) 
                temp = temp+get_values(image,i-1,j-4,size)
                temp = temp+get_values(image,i,j-4,size)
                temp = temp+get_values(image,i+1,j-4,size)
                temp = temp+get_values(image,i+2,j-4,size)
                temp = temp+get_values(image,i+3,j-4,size)
                temp = temp+get_values(image,i+4,j-4,size)
                med = np.median(temp)
                filter_image[i, j]= int(med)
                

    return filter_image
    


img = cv2.imread('image.jpg',0)
plt.imshow(img)
plt.show()
filtered_image = avg_filter(img,7)
cv2.imwrite("Result_median_7x7.jpg",filtered_image)

plt.imshow(filtered_image)
plt.show()