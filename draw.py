import numpy as np
import cv2

# [0, 0, 0]
# [0, 1, 0]
# [1, 1, 0]
# [1, 0, 0]
# [0, 0, 1]
# [0, 1, 1]
# [1, 1, 1]
# [1, 0, 1]

def draw(img, corners, imgpts):
    corner = tuple(corners[0][0].ravel())
    corner1 = tuple(corners[0][1].ravel())
    corner2 = tuple(corners[0][2].ravel())
    corner2 = tuple(corners[0][3].ravel())

    img = cv2.line(img, corner, corner1, (255,0,0), 5)
    img = cv2.line(img, corner, corner2, (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img


def drawCube(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)

    img = cv2.drawContours(img, [imgpts[:4]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[[1,2,6,5],:]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[[2,6,7,3],:]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[[3,7,4,0],:]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[[0,1,5,4],:]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[4:]],-1,(255,0,0),-3)
    img = cv2.drawContours(img, [imgpts[:4]],-1,(255,0,0),1)
    img = cv2.drawContours(img, [imgpts[[1,2,6,5],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[2,6,7,3],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[3,7,4,0],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[0,1,5,4],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,0),1)
    return img

def drawPyramid(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)

    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    img = cv2.drawContours(img, [imgpts[[0,1,4],:]],-1,(0,255,0),-3)
    img = cv2.drawContours(img, [imgpts[[0,3,4],:]],-1,(0,255,0),-3)
    img = cv2.drawContours(img, [imgpts[[1,2,4],:]],-1,(0,255,0),-3)
    img = cv2.drawContours(img, [imgpts[[2,3,4],:]],-1,(0,255,0),-3)
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[0,1,4],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[0,3,4],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[1,2,4],:]],-1,(0,0,0),1)
    img = cv2.drawContours(img, [imgpts[[2,3,4],:]],-1,(0,0,0),1)

    return img


