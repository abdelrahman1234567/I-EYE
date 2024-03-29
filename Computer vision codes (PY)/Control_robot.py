#---------------Required libraries---------------#
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import pyautogui as mouse
import sys
import serial
#------------------------------------------------#

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def send(x):
    arduino.write(bytes(x, 'utf-8'))

ap = argparse.ArgumentParser()
ap.add_argument(
    "-p", "--shape-predictor", required=True, help="path to facial landmark predictor"
)
ap.add_argument("-v", "--video", type=str, default="", help="path to input video file")
args = vars(ap.parse_args())

arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1)

EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 3

LeftBlink=0
RightBlink=0
tRightBlink=0
tLeftBlink=0

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])


(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


print("[INFO] starting video stream thread...")
vs = FileVideoStream(args["video"]).start()
fileStream = True
vs = VideoStream(src=0).start()
fileStream = False
time.sleep(1.0)

lastx=-1
lasty=-1

mouse.moveTo(683, 384)

while True:

    if fileStream and not vs.more():
        break

    frame = vs.read()
    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        x= (leftEye[0][0]+leftEye[3][0]+rightEye[0][0]+rightEye[3][0])/4.0
        y= (leftEye[0][1]+leftEye[3][1]+rightEye[0][1]+rightEye[3][1])/4.0

        #print("x: ",x,", y: ",y)
        #print("lastX: ",lastx,", lastY: ",lasty)
        if lastx == -1:
            lastx=x
            lasty=y
        if x>lastx-20 and x < lastx+20 and y>lasty-20 and y<lasty+20:
            send("sssssssss")
            #print("STOP")
        else:
            if x < lastx-20:
                send("llllllll")
                #print("LEFT")
            elif x>lastx+20:
                send("rrrrrrrr")
                #print("RIGHT")
            if y<lasty-20:
                send("ffffffff")
                #print("FORWARD")
            elif y>lasty+20:
                send("bbbbbbbb")
                #print("BACKWARD")
        
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


cv2.destroyAllWindows()
vs.stop()

# python control_robot.py --shape-predictor eye-detection-model.dat
