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

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)


axis = np.float32([[1, 0, 0], [0, 1, 0], [0, 0, -0.1]]).reshape(-1, 3)

cubePoints = np.float32([[0,0,0], [0,0.1,0], [0.1,0.1,0], [0.1,0,0],
                   [0,0,0.1],[0,0.1,0.1],[0.1,0.1,0.1],[0.1,0,0.1] ])
cubePoints = cubePoints - [0.05, 0.05, 0.]

pyraPoints = np.float32([[0,0,0], [0,0.1,0], [0.1,0.1,0], [0.1,0,0],
                   [0.05,0.05,0.1]])
pyraPoints = pyraPoints - [0.05, 0.05, 0.]

cv2.namedWindow("Mac Camera")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # pauses to make sure the frame can be read
    rval, frame = vc.read()
else:
    rval = False

while rval:

    rvecs = np.empty((0, 1, 3))
    tvecs = np.empty((0, 1, 3))

    rval, frame = vc.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)
    if np.all(ids is not None):

        for i in range(ids.size):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners[i], 0.1, mtx, dist)

            rvecs = np.vstack((rvecs, rvec))
            tvecs = np.vstack((tvecs, tvec))

        ind = np.argsort(tvecs[:, 0, 2])[::-1]
        tvecs = tvecs[ind]
        rvecs = rvecs[ind]

        if(ids.size == ind.size):
            ids = ids[ind]

        for i in range(ids.size):
            if ids[i] == 0:
                imgpts, _ = cv2.projectPoints(
                    cubePoints, rvecs[i], tvecs[i], mtx, dist)
                frame = drawCube(frame, corners[i].astype(int), imgpts.astype(int))

            if ids[i] == 1:
                imgpts, _ = cv2.projectPoints(
                    pyraPoints, rvecs[i], tvecs[i], mtx, dist)
                frame = drawPyramid(frame, corners[i].astype(int), imgpts)

    frame = cv2.flip(frame, 1)
    cv2.imshow("Mac Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyWindow("Mac Camera")
