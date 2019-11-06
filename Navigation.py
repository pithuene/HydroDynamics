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

pi = 3.141592564
wheelCircumference = pi * wheelDiameter                         # Berechnung des Umfangs des Rads
turnCircumference = pi * axleTrack                              # Berechnung des Umfangs des Drehkreises


motorWheelRight = Motor(Port.D)
motorWheelLeft = Motor(Port.A)

db = DriveBase(motorWheelLeft, motorWheelRight, wheelDiameter, axleTrack)
gs = GyroSensor(Port.S2)

'''
Variablen zur verwendung in der Drehung
'''
turn_try = False

'''
Variablen zur Orientierung auf dem Speilfeld
'''
lookingDirection = 0
startPoint = [0, 0] #Startpunkt immer Gleich (Anhand Raster auf dem Spielfeld)
currentPosition = startPoint

M03 = [[0, 0], [2.8, 0], [2.8, 6.475]]

def main():
    readNextPoint(M03) #Einlesen der Koordinaten um eine Aufgabe zu erreichen

'''
Auslesen der Koordinaten aus dem mitgegebenen Array
'''
def readNextPoint(pointArray):
    global currentPosition
    global wheelCircumference
    global lookingDirection
    localWheelCircumference = wheelCircumference / 10           # Umrechnung des Reifen Durchmessers in cm

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
                if lookingDirection != 0:                       # Wenn nach -x gesehen wird drehe nach x
                    #print("1")
                    turn(lookingDirection)
                    lookingDirection = 0
            elif currentPosition[0] > x:
                if lookingDirection != 180:                     # Wenn nach x gesehen wird drehe nach -x
                    #print("2")
                    turn( - (180 - lookingDirection))
                    lookingDirection = 180

            degree = (x * 10) / localWheelCircumference * 360
            driveForward(100, degree)
        
        '''
            Drehung zu der nächsten Koordinate auf der y-Achse
            Ausführen wenn nicht bereits in Blickrichtung
        '''
        if y != currentPosition[1]:
            if currentPosition[1] < y:                          # Wenn Blickrichtung um 180° gedreht
                if lookingDirection != 90:                      # Wenn nach -y gesehen wird drehe nach y
                    #print("3")
                    turn( - (90 - lookingDirection))
                    lookingDirection = 90
            elif currentPosition[1] > y:
                if lookingDirection != 270:                     # Wenn nach y gesehen wird drehe nach -y
                    #print("4")
                    turn( - (270 - lookingDirection))
                    lookingDirection = 270

            degree = (y * 10) / localWheelCircumference * 360
            driveForward(100, degree)

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

    gs.reset_angle(0)                                               # setzt die Gradzahl des Gyrosensors auf 0 vor jeder Drehung 
    
    turnAngleDist = turnCircumference / 360.0 * angle               # Berechnung der Entfernung die zurückgelegt werden muss bei einer Drehung
    turnAngle = turnAngleDist / wheelCircumference * 360            # Berechnung der Gradzahl für die zurückgelegte Entfernung
    
    motorWheelLeft.run_angle(speed, turnAngle, Stop.BRAKE, False)   # Wenn Gradzahl des Gyrosensors und Drehung nicht übereinstimmen -> Vorzeichen von turnAngle umtauschen 
    motorWheelRight.run_angle(speed, -turnAngle, Stop.BRAKE, True)
    check_angle(angle)

'''
Methode, welche dafür sorgt das der Roboter für eine halbe Sekunde vorwärts fährt und dann eine erneute Drehung ausführt 
'''

def test_turn_try(angle, turned_angle):

    global turn_try

    #print("####")
    db.drive_time(100,0,500)
    
    dif_angle = angle - turned_angle
    turn(dif_angle)

'''
Prüfen ob die gemessene Drehung mit der Vorgabe übereinstimmt
Wenn Abweichungen von 2 auftauchen sollten wird nachkorrigiert
'''

def check_angle(angle):

    global turn_try

    #print("----------------")
    #print(str(gs.angle()) + " -> " + str(angle))
    #print(turn_try)

    turned_angle = gs.angle()


    if turned_angle > angle + 2:
        if abs(turned_angle) <= 15:                 # Falls der Roboter eine von 15° unterschreitet wird die Methode test_turn_try aufgerufen 
            test_turn_try(angle, turned_angle)
        else:
            dif_angle = turned_angle - angle        # Berechnung der noch zu drehenden Gradzahl
            
            turn(-dif_angle)                        # Aufruf der Methode turn mit der neuen Gradzahl

    elif turned_angle < angle - 2:
        if abs(turned_angle) <= 15:
            test_turn_try(angle, turned_angle)
        else:
            dif_angle = angle - turned_angle
            
            turn(dif_angle)

'''
Methode zum Vorfährtsfahren - gemessen anhand von der Umdrehungsgradzahl (degree) und Geschwindigkeit mm/s (speed)
'''
def driveForward(speed, degree):
    motorWheelLeft.run_angle(speed, degree, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, degree, Stop.BRAKE, True)

main()
