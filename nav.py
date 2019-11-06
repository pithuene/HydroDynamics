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
    readNextPoint(pointArray)


'''
Auslesen der Koordinaten aus dem mitgegebenen Array
'''


def readNextPoint(pointArray):
    global currentPosition
    global wheelCircumference
    global lookingDirection
    # Umrechnung des Reifen Durchmessers in cm
    localWheelCircumference = wheelCircumference / 10

    i = 1
    while(i < len(pointArray)):                                 # Für jede Koordinate im Array
        nextPoint = pointArray[i]
        x = nextPoint[0]
        y = nextPoint[1]
        #print("x: " + str(x) + " y: " + str(y))
        #print("currentPosition: " + str(currentPosition[0]))

        '''
            Drehung zu der nächsten Koordinate auf der x-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if x != currentPosition[0]:
            # Wenn Blickrichtung um 180° gedreht
            if currentPosition[0] < x:
                if lookingDirection != 0:                       # Wenn nach -x gesehen wird drehe nach x
                    # print("1")
                    turn(lookingDirection)
                    lookingDirection = 0
            elif currentPosition[0] > x:
                if lookingDirection != 180:                     # Wenn nach x gesehen wird drehe nach -x
                    # print("2")
                    turn(- (180 - lookingDirection))
                    lookingDirection = 180

            degree = (x * 10) / localWheelCircumference * 360
            driveForward(degree, 100)

        '''
            Drehung zu der nächsten Koordinate auf der y-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if y != currentPosition[1]:
            # Wenn Blickrichtung um 180° gedreht
            if currentPosition[1] < y:
                if lookingDirection != 90:                      # Wenn nach -y gesehen wird drehe nach y
                    # print("3")
                    turn(- (90 - lookingDirection))
                    lookingDirection = 90
            elif currentPosition[1] > y:
                if lookingDirection != 270:                     # Wenn nach y gesehen wird drehe nach -y
                    # print("4")
                    turn(- (270 - lookingDirection))
                    lookingDirection = 270

            degree = (y * 10) / localWheelCircumference * 360
            driveForward(degree, 100)

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
Methode zum Vorfährtsfahren - gemessen anhand von der Umdrehungsgradzahl (degree) und Geschwindigkeit mm/s (speed)
'''


def driveForward(angle, speed=50):
    motorWheelLeft.run_angle(speed, angle, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, angle, Stop.BRAKE, True)
