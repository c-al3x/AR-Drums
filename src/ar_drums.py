from imutils.video import VideoStream

import argparse
import datetime
import imutils
import time
import cv2
import os
import contextlib
import numpy as np
import drums
import video

metadata, vid, kit = None, None, None

def prepareFrame():
    global vid
    global kit

    # grab the current frame
    frame = vid.input.read()
    frame = frame if vid.isStream else frame[1]

    # if the frame could not be grabbed, then we have reached the end
    # of the video
    if frame is None:
        return [], []

    # resize the frame, convert it to grayscale, and blur it
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    bluecnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # if the first frame is None, initialize it with its resolution and create drum layout
    if vid.firstFrame is None:
        vid.setFirstFrame(frame)
        vid.setRes(frame.shape)
        kit = drums.DrumKit(vid)

    drumParts = kit.getDrums()
    for drum in drumParts:
        topLeft, botRight, color = drum.getTopLeft(), drum.getBotRight(), drum.getColor()
        cv2.rectangle(frame, topLeft, botRight, color, 2)

    return frame, bluecnts

def contourLoop(frame, cnts):
    global metadata
    global kit

    for bluecnt in cnts:
        if cv2.contourArea(bluecnt) < metadata["min-area"]:
            continue
        (x, y, w, h) = cv2.boundingRect(bluecnt)
        x += int(w / 2)
        y += int(h / 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        drumParts = kit.getDrums()
        for drum in drumParts:
            leftX, rightX = drum.getLeftX(), drum.getRightX()
            topY, botY = drum.getTopY(), drum.getBotY()
            extraY = 0.3 * vid.getRes()[0]
            readyY = topY - extraY
            state = drum.getStatus()
            if (leftX <= x and x <= rightX and readyY <= y and y <= topY):
                drum.setStatus("ready")
            elif (leftX <= x and x <= rightX and topY <= y and y <= (botY + extraY)):
                if (state == "ready" and state != "hit"):
                    drum.play(); drum.setStatus("hit")
                    break
            elif (state != "ready"):
                drum.setStatus("inactive")

def finishFrame(frame):
    # Mirror the frame
    flipped_frame = cv2.flip(frame,1)
    cv2.imshow("Security Feed", flipped_frame)
    key = cv2.waitKey(1) & 0xFF
    return key

# loop over the frames of the video
def main():
    while True:
        frame, contours = prepareFrame()
        if len(frame) == 0: break
        if len(contours) != 0: contourLoop(frame, contours)
        userInput = finishFrame(frame)
        if userInput == ord("q"): break

def setup():
    global metadata
    global vid
    global kit

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the video file")
    ap.add_argument("-a", "--min-area", type=int, default=200, help="minimum area size")
    args = vars(ap.parse_args())

    metadata = {"min-area": args.get("min_area", None)}

    isStream = args.get("video", None) is None
    vid = video.Video(isStream, args)

def close():
    # cleanup the camera and close any open windows
    vid.close()

if __name__ == '__main__':
    setup()
    main()
    close()
