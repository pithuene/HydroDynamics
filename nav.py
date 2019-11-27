#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep
import array as arr

# Write your program here
brick.sound.beep()

'''
    Globale Variablen
        Sensoren und deren Ports
'''
wheelDiameter = 55  # Rad drehung = 17cm
axleTrack = 107  # 150  # 119

pi = 3.1415926536
# Berechnung des Umfangs des Rads
wheelCircumference = pi * wheelDiameter
# Berechnung des Umfangs des Drehkreises
turnCircumference = pi * axleTrack


motorWheelRight = Motor(Port.B)
motorWheelLeft = Motor(Port.A)

db = DriveBase(motorWheelLeft, motorWheelRight, wheelDiameter, axleTrack)

'''
Variablen zur Orientierung auf dem Speilfeld
'''
lookingDirection = 0
# Startpunkt immer Gleich (Anhand Raster auf dem Spielfeld)
startPoint = [0, 0]
currentPosition = startPoint

'''
Erhält einen Pfad in Form eines 2D Arrays von Punkten (x,y Koordinaten) die nacheinander abgefahren werden.
Dabei wird der Startpunkt [0,0] mit aufgenommen.

Beispiel:
[[0, 0], [2.8, 0], [2.8, 6.475]]
'''


def followCoordinatePath(pointArray):
    readNextPoint(pointArray, False)


def returnToStart(pointArray):
    returnArray = []
    i = len(pointArray) - 1
    # print(i)
    while(i >= 0):
        # print("NexPoint: " + str(pointArray[i][0]) + " " + str(pointArray[i][1]))
        returnArray.append(pointArray[i])
        i = i - 1

    readNextPoint(returnArray, True)


'''
Auslesen der Koordinaten aus dem mitgegebenen Array
'''


def readNextPoint(pointArray, returnPath):
    global currentPosition
    global wheelCircumference
    global lookingDirection
    localLookingDirection = lookingDirection

    if(returnPath == True):
        if(lookingDirection == 0):
            localLookingDirection = 180
        if(lookingDirection == 90):
            localLookingDirection = 270
        if(lookingDirection == 180):
            localLookingDirection = 0
        if(lookingDirection == 270):
            localLookingDirection = 90

    # Umrechnung des Reifen Durchmessers in cm
    localWheelCircumference = wheelCircumference / 10
    speed = 200

    i = 1
    while(i < len(pointArray)):                                 # Für jede Koordinate im Array
        # print(lookingDirection)
        if(i != 1):
            localLookingDirection = lookingDirection
        nextPoint = pointArray[i]
        x = nextPoint[0]
        y = nextPoint[1]
        # print("x: " + str(x) + " y: " + str(y))
        # print("currentPosition: " + str(currentPosition[0]))

        '''
            Drehung zu der nächsten Koordinate auf der x-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if x != currentPosition[0]:
            #print("x : " + str(x) + " Pos: " + str(currentPosition[0]))
            # Wenn Blickrichtung um 180° gedreht
            if currentPosition[0] < x:
                if localLookingDirection != 0:                       # Wenn nach -x gesehen wird drehe nach x
                    # print("1")
                    if(localLookingDirection == 270):
                        turn(180 - localLookingDirection)

                    else:
                        turn(localLookingDirection)

                    lookingDirection = 0

            elif currentPosition[0] > x:
                if localLookingDirection != 180:                     # Wenn nach x gesehen wird drehe nach -x
                    # print("2")
                    turn(- (180 - localLookingDirection))
                    lookingDirection = 180

            degree = abs((x * 10) / localWheelCircumference * 360)
            if(returnPath == False):
                driveForward(degree, speed)
            else:
                if (x == 0):
                    degree = abs(
                        (currentPosition[0] * 10) / localWheelCircumference * 360)
                driveForward(degree, speed * (-1))

        '''
            Drehung zu der nächsten Koordinate auf der y-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if y != currentPosition[1]:
            # Wenn Blickrichtung um 180° gedreht
            if currentPosition[1] < y:
                if localLookingDirection != 90:                      # Wenn nach -y gesehen wird drehe nach y
                    # print("3")
                    turn(- (90 - localLookingDirection))
                    lookingDirection = 90

            elif currentPosition[1] > y:
                if localLookingDirection != 270:                     # Wenn nach y gesehen wird drehe nach -y
                    # print("4")
                    if (localLookingDirection == 0):
                        turn(90 - localLookingDirection)

                    else:
                        turn(- (270 - localLookingDirection))

                    lookingDirection = 270

            degree = abs((y * 10) / localWheelCircumference * 360)
            if(returnPath == False):
                driveForward(degree, speed)
            else:
                if (y == 0):
                    degree = abs(
                        (currentPosition[1] * 10) / localWheelCircumference * 360)
                driveForward(degree, speed * (-1))

        currentPosition = nextPoint

        i = i + 1


'''
Methode um den Roboter zu drehen
angle gibt die Richtungsänderung an in Grad
    negative Werte sind Drehungen nach links
    positive Werte sind Drehungen nach rechts
speed gibt die Geschwindigkeit in mm/s an
'''


def turn(angle, speed=50):
    global wheelCircumference
    global turnCircumference

    # Berechnung der Entfernung die zurückgelegt werden muss bei einer Drehung
    turnAngleDist = turnCircumference / 360.0 * angle
    # Berechnung der Gradzahl für die zurückgelegte Entfernung
    turnAngle = turnAngleDist / wheelCircumference * 360

    # Wenn Gradzahl des Gyrosensors und Drehung nicht übereinstimmen -> Vorzeichen von turnAngle umtauschen
    motorWheelLeft.run_angle(speed, turnAngle, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, -turnAngle, Stop.BRAKE, True)


'''
Methode zum Vorwährtsfahren - gemessen anhand von der Umdrehungsgradzahl (degree) und Geschwindigkeit mm/s (speed)
'''


def driveForward(angle, speed=200):
    motorWheelLeft.run_angle(speed, angle, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, angle, Stop.BRAKE, True)


'''
Methode zum Vorwährtsfahren - Distanz in cm (distance) und Geschwindigkeit in mm/s (speed)
'''


def driveDistance(distance, speed=200):
    if(distance >= 0):
        db.drive_time(speed, 0, abs(distance)/speed*1000)
    else:
        db.drive_time(-speed, 0, abs(distance)/speed*1000)
    db.stop(Stop.BRAKE)
