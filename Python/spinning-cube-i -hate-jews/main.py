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

        self.translateX, self.translateY = (self.width - 4)//2, (self.height - 4)//2
        self.line_char = chr(23)

        self.X_rotate_speed = 0.03
        self.Y_rotate_speed = 0.08
        self.Z_rotate_speed = 0.13

        self.x = 0
        self.y = 1
        self.z = 2

    def line(self, x1, y1, x2, y2):
        points = []

        if (x1 == x2 and y1 == y2+1) or (y1 == y2 and x1 == x2+1):
            return [(x1, y1), (x2, y2)]
        
        isStep = abs(y2 - y1) > abs(x2 - x1)
        
        if isStep:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        
        isReversed = x1 > x2

        if isReversed:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

            deltax = x2 - x1
            deltay = abs(y2 - y1)
            extray = int(deltax)
            currenty = y2

            if y1 < y2:
                ydirection = 1
            else:
                ydirection = -1

            for currentx in range(x2, x1-1, -1):
                if isStep:
                    points.append((currenty, currentx))
                else:
                    points.append((currentx, currenty))
                extray -= deltay
                if extray <=0:
                    currenty -= ydirection
                    extray += deltax
        else:
            deltax = x2 - x1
            deltay = abs(y2 - y1)
            extray = int(deltax / 2)
            currenty = y1

            if y1 < y2:
                ydirection = 1
            else:
                ydirection = -1

            for currentx in range(x1, x2 +1):
                if isStep:
                    points.append((currenty, currentx))
                else:
                    points.append((currentx, currenty))

                extray -= deltay
                if extray < 0:
                    currenty += ydirection
                    extray += deltax
            
        return points

    def rotatePoints(self, x, y , z, ax, ay, az):
        
        rotatedX = x
        rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
        rotatedZ = (y * math.sin(ax)) - (z * math.cos(ax))
        x, y, z = rotatedX, rotatedY, rotatedZ


        rotatedX = (z * math.sin(ay)) - (x * math.cos(ay))
        rotatedY = y
        rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))

        rotatedX = (x * math.cos(az)) - (y * math.sin(az))
        rotatedY = (x * math.sin(az)) - (y * math.cos(az))
        rotatedZ = z

        return (rotatedX, rotatedY, rotatedZ)

    def adjustPoints(self, points):
        return (int(points[self.x] * self.scaleX + self.translateX),
                int(points[self.y] * self.scaleY + self.translateY))




CUBE_CORNERS = [[-1, -1, -1], 
                [ 1, -1, -1], 
                [-1, -1,  1], 
                [ 1, -1,  1], 
                [-1,  1, -1], 
                [ 1,  1, -1], 
                [-1,  1,  1], 
                [ 1,  1,  1]] 

rotated_corners = [None, None, None, None, None, None, None, None]

cube = Cube()

xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True:
        xRotation += cube.X_rotate_speed
        yRotation += cube.Y_rotate_speed
        zRotation += cube.Z_rotate_speed

        for i in range(len(CUBE_CORNERS)):
            cube.x = CUBE_CORNERS[i][cube.x]
            cube.y = CUBE_CORNERS[i][cube.y]
            cube.z = CUBE_CORNERS[i][cube.z]

            rotated_corners[i] = cube.rotatePoints(cube.x, cube.y, cube.z, xRotation, yRotation, zRotation)

        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            fromX, fromY = cube.adjustPoints(rotated_corners[fromCornerIndex])
            toX, toY = cube.adjustPoints(rotated_corners[toCornerIndex])
            pointsOnLine = cube.line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        cubePoints = tuple(frozenset(cubePoints))

        for y in range(cube.height):
            for x in range (cube.width):
                if(x, y) in cubePoints:
                    print(cube.line_char, end='', flush=False)
                else:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl+C to quit', end='', flush=True)

        time.sleep(cube.pause)

        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    print('\nRotating cube by Majster, Github: https://github.com/HansPanzer2137')
    sys.exit()


