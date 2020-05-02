from cv2 import VideoCapture,imwrite
cam = VideoCapture(0)
s, img = cam.read()
imwrite("capture.jpg",img)
del(cam)