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
wheelDiameter = 55                                              #Rad drehung = 17cm
axleTrack = 107  # 150  # 119

pi = 3.1415926536
wheelCircumference = pi * wheelDiameter                         # Berechnung des Umfangs des Rads
turnCircumference = pi * axleTrack                              # Berechnung des Umfangs des Drehkreises


motorWheelRight = Motor(Port.B)
motorWheelLeft = Motor(Port.A)

db = DriveBase(motorWheelLeft, motorWheelRight, wheelDiameter, axleTrack)

'''
Variablen zur Orientierung auf dem Speilfeld
'''
lookingDirection = 0
startPoint = [0, 0] #Startpunkt immer Gleich (Anhand Raster auf dem Spielfeld)
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
    print(i)
    while(i >= 0):
        #print("NexPoint: " + str(pointArray[i][0]) + " " + str(pointArray[i][1]))
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

    localWheelCircumference = wheelCircumference / 10           # Umrechnung des Reifen Durchmessers in cm
    speed = 200

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
            if currentPosition[0] < x:                          # Wenn Blickrichtung um 180° gedreht
                if localLookingDirection != 0:                       # Wenn nach -x gesehen wird drehe nach x
                    #print("1")
                    turn(localLookingDirection)
                    lookingDirection = 0
            elif currentPosition[0] > x:
                if localLookingDirection != 180:                     # Wenn nach x gesehen wird drehe nach -x
                    #print("2")
                    turn( - (180 - localLookingDirection))
                    lookingDirection = 180

            degree = (x * 10) / localWheelCircumference * 360
            if(returnPath == False):
                driveForward(degree, speed)
            else:
                if (x == 0):
                    degree = (currentPosition[0] * 10) / localWheelCircumference * 360
                driveForward(degree, speed * (-1))
        
        '''
            Drehung zu der nächsten Koordinate auf der y-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if y != currentPosition[1]:
            if currentPosition[1] < y:                          # Wenn Blickrichtung um 180° gedreht
                if localLookingDirection != 90:                      # Wenn nach -y gesehen wird drehe nach y
                    #print("3")
                    turn( - (90 - localLookingDirection))
                    lookingDirection = 90
            elif currentPosition[1] > y:
                if localLookingDirection != 270:                     # Wenn nach y gesehen wird drehe nach -y
                    #print("4")
                    turn( - (270 - localLookingDirection))
                    lookingDirection = 270

            degree = (y * 10) / localWheelCircumference * 360
            if(returnPath == False):
                driveForward(degree, speed)
            else:
                if (y == 0):
                     degree = (currentPosition[1] * 10) / localWheelCircumference * 360
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

def turn(angle, speed = 50):
    global wheelCircumference
    global turnCircumference
    
    turnAngleDist = turnCircumference / 360.0 * angle               # Berechnung der Entfernung die zurückgelegt werden muss bei einer Drehung
    turnAngle = turnAngleDist / wheelCircumference * 360            # Berechnung der Gradzahl für die zurückgelegte Entfernung
    
    motorWheelLeft.run_angle(speed, turnAngle, Stop.BRAKE, False)   # Wenn Gradzahl des Gyrosensors und Drehung nicht übereinstimmen -> Vorzeichen von turnAngle umtauschen 
    motorWheelRight.run_angle(speed, -turnAngle, Stop.BRAKE, True)


'''
Methode zum Vorfährtsfahren - gemessen anhand von der Umdrehungsgradzahl (degree) und Geschwindigkeit mm/s (speed)
'''
def driveForward(angle, speed = 200):
    motorWheelLeft.run_angle(speed, angle, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, angle, Stop.BRAKE, True)
