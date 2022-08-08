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
#------------------------------------------------#

def eye_aspect_ratio(eye): #Function to calculate eye aspect rateio
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def translate(value, leftMin, leftMax, rightMin, rightMax):  #Function to translate a range to other range
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

ap = argparse.ArgumentParser()
ap.add_argument(
    "-p", "--shape-predictor", required=True, help="path to facial landmark predictor"
)
ap.add_argument("-v", "--video", type=str, default="", help="path to input video file")
args = vars(ap.parse_args())

#------Initalizing variables-------#
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 3

LeftBlink=0
RightBlink=0
tRightBlink=0
tLeftBlink=0

last_mousex = -1
last_mousey = -1

lastx=-1
lasty=-1
flag = 0
#----------------------------------#

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

mouse.moveTo(990, 540)

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

        #Getting the coordinates of the six points and calculating eye aspect ratio
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        #Drawing the countours arount the eye to mark it
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        #print("leftEAR: ",leftEAR,", righEAR: ",rightEAR)

        #Checking the eye aspect ration to detect the blink and diffrenciate between it and the normal blink
        if leftEAR<0.19 and leftEAR<rightEAR:
            LeftBlink+=1

        else:
            if LeftBlink >= EYE_AR_CONSEC_FRAMES:
                mouse.click()
                tLeftBlink+=1
            LeftBlink=0

        if rightEAR<0.19 and leftEAR>rightEAR:
            RightBlink+=1

        else:
            if RightBlink >= EYE_AR_CONSEC_FRAMES:
                tRightBlink+=1
                mouse.click(button = 'right')
            RightBlink=0

        #Calculating the average coordinates of the eye using the coordinates of the six points
        x= (((leftEye[0][0]+leftEye[3][0])/2.0)+((rightEye[0][0]+rightEye[3][0])/2.0))/2.0
        y= (((leftEye[0][1]+leftEye[3][1])/2.0)+((rightEye[0][1]+rightEye[3][1])/2.0))/2.0 
        
        if flag == 0:
            flag=1
            lastx = x 
            lasty = y

        #Translating the coordinates of the eye to the coordinates of the mouse
        mousex = 1860-translate(x,lastx-40,lastx+40,10,1860)
        mousey = translate(y,lasty-25,lasty+25,10,960)

        if last_mousex == -1:
            last_mousex = mousex
            last_mousey = mousey
        
        #Putting limits for the mouse coordinates to not getting outside the border
        if mousex < 10:
            mousex=10
        elif mousex >1960:
            mousex=1960
        if mousey < 10:
            mousey=10
        elif mousey >1050:
            mousey=1050
        
        if abs(last_mousex - mousex) > 20 or abs(last_mousey - mousey) > 20:
            mouse.moveTo(mousex, mousey) #Moving the mouse to the required coordinates
        last_mousex = mousex
        last_mousey = mousey
        
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


cv2.destroyAllWindows()
vs.stop()

# python control_mouse.py --shape-predictor eye-detection-model.dat
