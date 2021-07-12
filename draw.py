import numpy as np
import cv2 as cv

def drawCube(img, imgpts):
    bottom = np.int32(imgpts).reshape(-1, 2)

    img = cv.drawContours(img, [bottom[:4]], -1, (0, 255, 0), -3)

    
    top = np.vstack((bottom[:,0],bottom[:,1] - 150))
    top = top.T 

    img = cv.drawContours(img, [top[:4]], -1, (0, 0, 255), 3)

    for i in range(4):
        img = cv.line(img, tuple(bottom[i]), tuple(top[i]), (255), 3)

    return img
