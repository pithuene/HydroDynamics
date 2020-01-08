#!/usr/bin/env pybricks-micropython

#import arm
import nav
#import color
import time
import tasks.M02
import tasks.M05
import tasks.M03

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

tasks.M05.main()
brick.sound.beep()
time.sleep(5)
nav.lookingDirection = 0
tasks.M03.main()
brick.sound.beep()
nav.lookingDirection = 0
time.sleep(5)
tasks.M02.main()
brick.sound.beep()
nav.lookingDirection = 0
