#Scaling, Translation, Rotation

import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils


def Translation(image,x = 1,y = 1):
    h,w = image.shape
    mat = np.float32([[1,0,x],[0,1,y]])
    trans = cv2.warpAffine(image,mat,(h,w))
    
    return trans

def Scaling(image,x = 1,y = 1):
    h,w = image.shape
    mat = np.float32([[x,0,0],[0,y,0]])
    scale = cv2.warpAffine(image,mat,(h,w))
    
    return scale 

def Rotation(image,theta = 0):
    h,w = image.shape
    rotate = imutils.rotate_bound(image,theta)
    
    return rotate



if __name__ == '__main__':

    img = cv2.imread('image.jpg',0)
    plt.imshow(img)
    plt.title('Original Image')
    plt.show()
    
    #Translation
    result = Translation(img,2)
    plt.imshow(result)
    plt.title('Translated Image')
    plt.show()
    
    #Scaling
    result = Scaling(img,2)
    plt.imshow(result)
    plt.title('Scaled Image')
    plt.show()
    
    #Rotation
    result = Rotation(img,-30)
    plt.imshow(result)
    plt.title('Rotated Image')
    plt.show()
    
    #All operations Combined
    Translate = Translation(img,2)
    Rotate = Rotation(Translate,-30)
    Scale = Scaling(Rotate,2)
    plt.imshow(Scale)
    plt.title('All operations Combined Image')
    plt.show()
    
    
    