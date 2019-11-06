#!/usr/bin/env pybricks-micropython

import arm
import nav

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

us = UltrasonicSensor(Port.S4)
motorWheelRight = Motor(Port.B)
motorWheelLeft = Motor(Port.A)

pi = 3.141592564

wheelDiameter = 55
axleTrack = 107  # 150  # 119


db = DriveBase(motorWheelLeft, motorWheelRight, wheelDiameter, axleTrack)


def turn(angle, speed=30):
    wheelCircumference = pi * wheelDiameter
    turnCircumference = pi * axleTrack
    turnAngleDist = turnCircumference / 360.0 * angle
    print('TurnAngleDist: ' + str(turnAngleDist))
    turnAngle = turnAngleDist / wheelCircumference * 360.0
    print('TurnAngle: ' + str(turnAngle))
    motorWheelLeft.run_angle(speed, turnAngle, Stop.BRAKE, False)
    motorWheelRight.run_angle(speed, -turnAngle, Stop.BRAKE, True)



def preciseDistance(ultrasonic, tries=5):
    sum = 0
    for i in range(0, tries):
        sum += ultrasonic.distance()
        wait(30)
    return sum / tries
