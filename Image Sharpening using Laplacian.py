#Image Sharpening using Laplacian Filter from scratch

import cv2
import matplotlib.pyplot as plt
import numpy as np

def display(image,Title = ''):
    plt.imshow(img)
    plt.title(Title)
    plt.show()
    

def conv2D(image, kernel):
    result = None
    kernel = np.flip(kernel)
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        result = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                result[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
    return result


if __name__ == '__main__':

    img = cv2.imread('Laplacian.png',0)
    img = img/255
    display(img,'Original Image')
    
    lap_filter = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    #lap_filter = np.array([[0,1,0],[1,4,1],[0,1,0]])
    #lap_filter = np.array([[1,0,1],[0,-4,0],[1,0,1]])
    filtered = conv2D(img,lap_filter)
    display(img,'Filtered Image')
    
    final = img[0:498,0:729]-filtered
    cv2.imwrite("Result_sharp.jpg",final)
    display(final,'Final Result')
    
    
    #cv2.imshow('Original Image',img)
    #cv2.imshow('Filtered Image',filtered)
    #cv2.imshow('Difference Image',diff)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

