import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from populationEnv import PopulationEnv
import cv2 as cv

popEnv = PopulationEnv()

def rescale(frame, scale=0.75):
    #images video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("animation.mp4")

while True:
    isReadable, frame = capture.read()

    resizedFrame = rescale(frame)
    # change_resolution(600, 600)
    
    # cv.imshow('My Video', frame)

    if isReadable:
        # frame = cv.GaussianBlur(frame, (15,15), cv.BORDER_DEFAULT)
    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
capture.destroyAllWindows()


#Ending wait key
cv.waitKey(0)