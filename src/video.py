from imutils.video import VideoStream

import argparse
import datetime
import imutils
import time
import cv2
import os
import contextlib
import numpy as np
#with contextlib.redirect_stdout(None):
#    from pygame import mixer

class Video:

    def __init__(self, isStream, args):
        self.isStream = isStream
        if isStream:
            self.input = VideoStream(src=0).start()
            time.sleep(2.0)
        else:
            self.input = cv2.VideoCapture(args["video"])
        self.resolution = (0, 0)
        self.firstFrame = None

    def getRes(self):
        return self.resolution

    def setRes(self, resolution):
        self.resolution = resolution

    def getFirstFrame(self):
        return self.firstFrame

    def setFirstFrame(self, frame):
        self.firstFrame = frame

    def close(self):
        if self.isStream:
            self.input.stop()
        else:
            self.input.release()
        cv2.destroyAllWindows()
