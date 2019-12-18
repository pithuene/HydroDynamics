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
import color
import utils

# Write your program here
brick.sound.beep()

'''
    Globale Variablen
        Sensoren und deren Ports
'''
wheelDiameter = 55  # Rad drehung = 17cm
axleTrack = 120  # Hildi: 105.5, Dieter: 120

pi = 3.1415926536
# Berechnung des Umfangs des Rads
wheelCircumference = pi * wheelDiameter
# Berechnung des Umfangs des Drehkreises
turnCircumference = pi * axleTrack

motorWheelRight = Motor(Port.B)
motorWheelLeft = Motor(Port.A)
sideUltrasonic = UltrasonicSensor(Port.S1)

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


def driveToBlack():
    color.driveToBlack(db, motorWheelLeft, motorWheelRight)


def followCoordinatePath(path: [Vector]):
    for point in path:
        driveToPoint(point)


def driveToPoint(point: Vector, checkBlackLines=True):
    global position
    print("Current Position " + str(position))
    print("Now driving to " + str(point))
    path = Line(position, point)
    direction = point - position
    turnToLookingDirection(direction.normalize())
    lineCross = willCrossBlackLine(position, point)
    if(checkBlackLines & (lineCross != None)):
        determinePositionOnNextBlackLine(lineCross)
        driveToPoint(point, False)
    else:
        driveDistance(path.length())


def getDistanceToWall():
    return (utils.preciseDistance(sideUltrasonic) / 10) + 6


def determinePositionOnNextBlackLine(blackLine):
    global position
    global lookingDirection
    color.driveToBlack(db, motorWheelLeft, motorWheelRight)
    newPosition = blackLine[1]
    print("Determining position on Black line")
    if(newPosition.x == 0):
        newPosition.x = getDistanceToWall()
        lookingDirection = Vector(0, 1)
    else:
        newPosition.y = getDistanceToWall()
        lookingDirection = Vector(1, 0)
    print("Determined: " + str(newPosition))
    print("Now looking towards: " + str(lookingDirection))
    position = newPosition


# If the Path will cross a black line, return that line as given
# in the list at the top


def willCrossBlackLine(currentPosition: Vector, nextPosition: Vector):
    drivePath = Line(currentPosition, nextPosition)
    for blackLine in blackLines:
        intersectionPoint = drivePath.intersects(blackLine[0])
        if(intersectionPoint != None):
            return blackLine
    return None


def turnToLookingDirection(direction: Vector):
    global lookingDirection
    print("Current looking direction: " + str(lookingDirection))
    destinationAngle = direction.toAngle()
    currentAngle = lookingDirection.toAngle()
    turnAngle = destinationAngle - currentAngle
    if turnAngle < 0:
        turnAngle += 360
    print("Turning by: " + str(turnAngle))
    turn(turnAngle)
    print("New looking direction: " + str(lookingDirection))


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
    global lookingDirection

    angle = angle % 360
    if(angle > 180):
        angle -= 360
    elif (angle < -180):
        angle += 360

    negativeAngle = (angle < 0)
    angle = abs(angle)
    currentAngle = lookingDirection.toAngle()
    print("Current angle: " + str(currentAngle))

    if(negativeAngle):
        newLookingDirection = Vector.fromAngle(
            currentAngle - angle).normalize()
    else:
        newLookingDirection = Vector.fromAngle(
            currentAngle + angle).normalize()
    print("New looking direction: " + str(newLookingDirection))

    # Berechnung der Entfernung die zurückgelegt werden muss bei einer Drehung
    turnAngleDist = turnCircumference / 360.0 * angle
    # Berechnung der Gradzahl für die zurückgelegte Entfernung
    turnAngle = turnAngleDist / wheelCircumference * 360

    # Wenn Gradzahl des Gyrosensors und Drehung nicht übereinstimmen -> Vorzeichen von turnAngle umtauschen
    if(negativeAngle):
        motorWheelLeft.run_angle(speed, -turnAngle, Stop.BRAKE, False)
        motorWheelRight.run_angle(speed, turnAngle, Stop.BRAKE, True)
    else:
        motorWheelLeft.run_angle(speed, turnAngle, Stop.BRAKE, False)
        motorWheelRight.run_angle(speed, -turnAngle, Stop.BRAKE, True)
    lookingDirection = newLookingDirection


'''
Methode zum Vorwährtsfahren - Distanz in cm (distance) und Geschwindigkeit in mm/s (speed)
'''


def driveDistance(distance, speed=200):
    global lookingDirection
    global position
    if(distance >= 0):
        db.drive_time(speed, 0, abs(distance*10)/speed*1000)
        position = position + (lookingDirection * (distance))
    else:
        db.drive_time(-speed, 0, abs(distance*10)/speed*1000)
        position = position - (lookingDirection * (distance))
    db.stop(Stop.BRAKE)
