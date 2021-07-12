import os.path
import cv2
import numpy as np
from numpy.core.arrayprint import printoptions
from calibration import calibrate
from draw import *


cv_file = cv2.FileStorage("./coefficients.yaml", cv2.FILE_STORAGE_READ)

# if(os.path.isfile("coefficients.yaml" == True)):
#     print("File found")
mtx = cv_file.getNode('K').mat()
dist = cv_file.getNode('D').mat()
cv_file.release()
# else:
#     print("Creating calibration file")
#     ret, mtx, dist, rvecs, tvecs = calibrate()
print(mtx)
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

cv2.namedWindow("Mac Camera")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # pauses to make sure the frame can be read
    rval, frame = vc.read()
else:
    rval = False

while rval:


    rval, frame = vc.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)
    if np.all(ids is not None):
        for i in range(0, len(ids)):
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(
                corners[i], 0.02, mtx, dist)
            (rvec - tvec).any()  # get rid of that nasty numpy value array error
        # frame_markers = cv2.aruco.drawDetectedMarkers(
        #     frame.copy(), corners, ids)
        # axis = cv2.aruco.drawAxis(frame, mtx, dist, rvec,
        #                           tvec, 0.01)  # Draw axis
        print(imgpts.shape)
        frame = drawCube(frame, imgpts)
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Mac Camera", frame)
    print("loop over")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyWindow("Mac Camera")
