# marker-based-ar

The main goal of the application is to implements marker based augmented reality that allows the inclusion of virtual elements aligned with real elements. Using the ArUco marker based library and OpenCV, we can managed to detect markers in a real image and draw 3D models in the same plan.

There are 2 parts of this application. The first one is happening offline, we use a sample of picture to find the intrinsic characteristics of the camera, the camera matrix and the distortion matrix. Once we have computed both of these, we can start with the live part which estimates the position of each marker with respect to the camera and allows us to render 3D objects in coordinate system with respect to those markers.
