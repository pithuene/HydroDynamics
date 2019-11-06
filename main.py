#!/usr/bin/env pybricks-micropython

import arm
import nav
import color

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

color.driveToBlack(nav.db, nav.motorWheelLeft, nav.motorWheelRight)
