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
from vector import Vector
from line import Line

# Write your program here
brick.sound.beep()

'''
    Globale Variablen
        Sensoren und deren Ports
'''
wheelDiameter = 55  # Rad drehung = 17cm
axleTrack = 120  # 150  # 119

pi = 3.1415926536
# Berechnung des Umfangs des Rads
wheelCircumference = pi * wheelDiameter
# Berechnung des Umfangs des Drehkreises
turnCircumference = pi * axleTrack

motorWheelRight = Motor(Port.B)
motorWheelLeft = Motor(Port.A)

db = DriveBase(motorWheelLeft, motorWheelRight, wheelDiameter, axleTrack)

position = Vector(18, 33.25)
lookingDirection = Vector(1, 0)


# Die lange Seite des Spielfelds ist die `x` Koordinate
# Die Ecke des Spielfelds in der Startzone ist 0/0
# Die Angaben Tupel, der erste Wert ist eine
# Linie die die schwarze Linie auf dem Spielfeld repräsentiert
# Der zweite Wert ist ein Vector, bei dem eine Koordinate 0 ist
# die zweite Koordinate gibt an, was über die Position des Roboters
# sicher ist, nachdem er sich an dieser Linie positioniert hat
blackLines = [
    # Mittlere Linie über grüne Rampe
    (Line(Vector(129.5, 0), Vector(129.5, 114)), Vector(129.5, 0)),
    # Linie am brennenden Haus
    (Line(Vector(183.5, 0), Vector(183.5, 39)), Vector(183, 5)),
    # Linie am Feuerwehrauto
    (Line(Vector(129.5, 73), Vector(156, 73)), Vector(0, 73)),
]


def addVec(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])


def compVec(vec1, vec2):
    return vec1[0] == vec2[0] & vec1[1] == vec2[1]


def betweenTwoNumbers(num, bet1, bet2):
    return ((bet1 < num) & (num < bet2)) | ((bet2 < num) & (num < bet1))

# If the Path will cross a black line, return that line as given
# in the list at the top


def willCrossBlackLine(currentPosition: Vector, nextPosition: Vector):
    drivePath = Line(currentPosition, nextPosition)
    for blackLine in blackLines:
        intersectionPoint = drivePath.intersects(blackLine[0])
        if(intersectionPoint != None):
            return blackLine
    return None


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
Methode zum Vorwährtsfahren - Distanz in cm (distance) und Geschwindigkeit in mm/s (speed)
'''


def driveDistance(distance, speed=200):
    if(distance >= 0):
        db.drive_time(speed, 0, abs(distance*10)/speed*1000)
    else:
        db.drive_time(-speed, 0, abs(distance*10)/speed*1000)
    db.stop(Stop.BRAKE)
    position = position + (lookingDirection * (distance*10))
