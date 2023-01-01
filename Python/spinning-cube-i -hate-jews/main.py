import time
import sys
import os
import math


class Cube:
    def __init__(self):
        self.pause = 0.1
        self.width, self.height = 80, 24

        self.scaleX, self.scaleY = (self.width - 4)//8 , (self.height - 4)//8
        self.scaleY *=2

        self.translateX, self.translateY