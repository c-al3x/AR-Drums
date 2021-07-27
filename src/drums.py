import os
import contextlib
import numpy as np
import pyglet


class DrumKit:

    def __init__(self, video):
        samplesPath = os.getcwd() + "/drum_samples/"
        specs = self.createSpecs()
        self.drumNames = specs.keys()

        self.drums = {}
        for name in self.drumNames:
            coordinates, color = specs[name]
            sound = pyglet.media.load(samplesPath + name + ".wav", streaming=False)
            for i in np.arange(4):
                coordinates[i] = int(coordinates[i] * video.getRes()[(i + 1) % 2])
            self.drums[name] = DrumKit.Drum(coordinates, color, sound)

    def createSpecs(self):
        specs = {
            "snare": np.array([[0.7, 0.60, 0.83, 0.63], (0, 0, 255)]),
            "hihat": np.array([[0.85, 0.4, 0.99, 0.43], (0, 255, 255)]),
            "kick": np.array([[0.35, 0.96, 0.4, 0.99], (180, 105, 255)]),
            "ride": np.array([[0.05, 0.3, 0.25, 0.33], (0, 128, 255)])
        }

        return specs

    def getNames(self):
        return self.drumNames

    def getDrum(self, name):
        return self.drums[name]

    def getDrums(self):
        return self.drums.values()

    class Drum:

        def __init__(self, coordinates, color, sound):
            self.coordinates = coordinates
            self.leftX, self.rightX = coordinates[0], coordinates[2]
            self.topY, self.botY = coordinates[1], coordinates[3]
            self.color = color
            self.sound = sound
            self.status = "inactive"

        def getLeftX(self):
            return self.leftX

        def getRightX(self):
            return self.rightX

        def getTopY(self):
            return self.topY

        def getBotY(self):
            return self.botY

        def getPos(self):
            return self.coordinates

        def getTopLeft(self):
            return self.getCorner(0)

        def getBotRight(self):
            return self.getCorner(2)

        def getCorner(self, index):
            x, y = self.coordinates[index], self.coordinates[index + 1]
            return (x, y)

        def getColor(self):
            return self.color

        def getSound(self):
            return self.sound

        def getStatus(self):
            return self.status

        def setStatus(self, status):
            if status in ["inactive", "ready", "hit"]:
                self.status = status

        def play(self):
            self.sound.play()
