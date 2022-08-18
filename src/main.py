from populationEnv import PopulationEnv
import cv2 as cv

#Creates a Simulation and Records a Video About it
popEnv = PopulationEnv()

def rescale(frame, scale=0.75):
    """
    Rescales the frame to a smaller size.
    Args:
        frame (np.array): Frame to be rescaled.
        scale (float): Scale to be used (in percentage from 0 to 1).
        Returns:the rezided frame.
    """
    #images video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

#Grabs the same video it creates
capture = cv.VideoCapture("animation.mp4")

i = 0
while True:
    isReadable, frame = capture.read()
    # resizedFrame = rescale(frame) (For your resizing needs of everyday!)
    
    day = "Day " + str(int(i))
    i += 0.20

    if isReadable:
        cv.putText(frame, day, (280, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()

#Ending wait key
cv.waitKey(0)